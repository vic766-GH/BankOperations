import json
import re
from collections import Counter
from operator import itemgetter
from pathlib import Path

import pandas as pd

from src.read_transactions import read_csv, read_xls

"""Модуль обеспечивающий функционал взаимодействия с пользователем для выбора источника данных по транзакциям, 
дальнейшей обработки полученных транзакций и вывода в консоль результатов работы где реальные данные маскируются 
особым, ранее определённым способом. Работа с модулем производится путём запуска основной программы в модуле main.py 
из корневого каталога проекта"""

def process_bank_search(operations_data: list[dict], state: str) -> list[dict]:
    """функция, принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании ('description') есть данная строка.
    """

    pattern = re.compile(state, re.IGNORECASE)
    sel_operations_data = [
        operation
        for operation in operations_data
        if re.search(pattern, str(operation["description"]))
    ]

    return sel_operations_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """функцию принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории. Категории операций хранятся в поле 'description'."""

    state_count = [state["state"] for state in data if state["state"] in categories]
    data_count = Counter(state_count)
    return dict(data_count)


def source_select(file_name: str) -> tuple[list, list[dict]]:
    """Функция выполняющая основной диалог с пользователем для выбора источника транзакций и вариантов его
    предварительной обработки (сортировка, выборка). Принимает в качестве аргумента путь и имя файла без расширения
    и возвращает список словарей транзакций, сформированный по требованиям пользователя
    """

    answers = []
    current_directory = Path.cwd()
    if file_name == "":
        source_dir = ""
    elif current_directory.stem == "BankOperations":
        source_dir = "data"
    else:
        source_dir = "../data"
    source_file = Path.joinpath(Path(source_dir), file_name)

    answers = get_variant()

    if answers[0] == "1":
        fn = f"{source_file}.json"
        try:
            # operations_data = json.load(open(fn, "r", encoding="UTF-8"))
            operations_data = json.load(open(fn, "r"))
        except FileNotFoundError, FileNotFoundError:
            print(f"Ошибка файла: {fn}")
            return answers[1], []

    elif answers[0] == "2":
        fn = f"{source_file}.csv"
        try:
            operations_data = read_csv(fn)
        except FileNotFoundError, FileNotFoundError:
            print(f"Ошибка файла: {fn}")
            return answers[1], []

    else:
        fn = f"{source_file}.xlsx"
        try:
            operations_data = read_xls(fn)
        except FileNotFoundError, FileNotFoundError:
            print(f"Ошибка файла: {fn}")
            return answers[1], []

    result_list = [
        operation for operation in operations_data if operation["state"] in answers[1]
    ]

    if answers[3].lower() == "по возрастанию":
        result_list.sort(key=itemgetter("date"))
    elif answers[3].lower() == "по убыванию":
        result_list.sort(key=itemgetter("date"), reverse=True)

    if answers[4].lower() == "да":
        result_list_rub = [
            trans_dict
            for trans_dict in result_list
            if trans_dict["currency_code"] == "RUB"
        ]
        result_list = result_list_rub

    if answers[5].lower() == "да":
        result_list = process_bank_search(result_list, state=answers[6])

    return answers[1], result_list


def print_select(result_list: list[dict], state_select: list) -> None:
    """Функция вывода в консоль результатов выборки транзакций. Принимает подготовленный список словарей транзакций
    и строку заданных категорий состояния"""

    print(f"Всего банковских операций в выборке: {len(result_list)}")
    print("Распечатываю итоговый список транзакций...\n")
    if len(result_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for operation in result_list:
            print(
                f"{pd.to_datetime(operation['date']):%d.%m.%Y} {operation['description']}"
            )
            try:
                empty_from = len(operation["from"])
            except TypeError:
                print(f"{mask_source(str(operation['to']))}")
            else:
                if empty_from > 0:
                    print(
                        f"{mask_source(str(operation['from']))} -> {mask_source(str(operation['to']))}"
                    )
                else:
                    print(f"{mask_source(str(operation['to']))}")
            print(f'Сумма: {int(operation['amount'])} {operation["currency_code"]}\n')

    print(
        f"Банковские операции по выбранным категориям: {process_bank_operations(result_list, state_select)}"
    )


def get_variant() -> list:
    """Функция опроса пользователя и получения параметров обработки транзакций"""

    selection = {"1": "JSON-файла", "2": "CSV-файла", "3": "XLSX-файла"}
    answers = ["", [], "", "", "", "", ""]
    # Диалог с пользователем и заполнение списка answers с ответами для дальнейшей обработки транзакций в source_select
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        answers[0] = input("""\nВыберите необходимый пункт меню:\n
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла\n>>>""")
        if answers[0] not in ("1", "2", "3"):
            if answers[0] in ("q", "quit"):
                raise SystemExit
            else:
                print(
                    'Вы ошиблись при выборе источника. Повторите ещё раз или нажмите "q" для выхода из программы'
                )
                continue
        else:
            print(f"Вы выбрали получение информации из {selection[answers[0]]}\n")
            break
    while True:
        all_available = True
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.\n")
        answer = input(
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n>>>"
        )
        answers[1] = re.split(r"[,\s]+", answer)
        for answer_1 in answers[1]:
            if answer_1.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
                all_available = False
                print(f'Статус операции "{answer_1}" недоступен.')
        if all_available:
            break
    print(f'Операции отфильтрованы по статусу "{answers[1]}"')

    answers[2] = input("Отсортировать операции по дате? Да/\033[1;4mНет\033[0m\n>>>")
    if answers[2] == "да":
        answers[3] = input(
            "Отсортировать по возрастанию или по убыванию? \033[1;4mпо возрастанию\033[0m/по "
            "убыванию\n>>>"
        )

    answers[4] = input(
        "Выводить только рублевые транзакции? Да/\033[1;4mНет\033[0m\n>>>"
    )

    answers[5] = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/\033[1;4mНет\033["
        "0m\n>>>"
    )
    if answers[5] == "да":
        answers[6] = input("Введите слово для поиска\n>>>")

    return answers


def mask_source(card_info: str) -> str:
    """Функция маскирования номера с помощью библиотеки 're'"""

    if len(card_info) == 0:  # Проверка пустой строки
        # print("Некорректные данные - Пустая строка")
        return ""
    if re.search(r"Счет|Счёт", card_info) is None:
        # str_account = re.search(r'\d{16}',card_info)
        return re.sub(
            r"(\d{4})(\d{2})(\d{2})(\d{4})(\d{4})", r"\1 \2** **** \4", card_info
        )
    else:
        # str_account = re.search(r'\d{20}',card_info)
        return re.sub(r"\d{16}", r"**", card_info)
