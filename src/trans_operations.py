import re
import json
import pandas as pd

from collections import Counter
from operator import itemgetter
from src.read_transactions import read_csv, read_xls
from src.widget import mask_account_card


def process_bank_search(operations_data: list[dict], state: str) -> list[dict]:
    """функция, принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании ('description') есть данная строка."""

    pattern = re.compile(state, re.IGNORECASE)
    sel_operations_data = [operation for operation in operations_data if re.search(pattern, str(operation[
        'description']))]

    return sel_operations_data

def process_bank_operations(data:list[dict], categories:list)->dict:
    """функцию принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории. Категории операций хранятся в поле 'description'."""

    state_count = [state['state'] for state in data if state['state'] in categories]
    data_count = Counter(state_count)
    return dict(data_count)



def source_select(file_name: str) -> tuple[list,list[dict]]:
    """Функция выполняющая основной диалог с пользователем для выбора источника транзакций и вариантов его
    предварительной обработки (сортировка, выборка). Принимает в качестве аргумента путь и имя файла без расширения
    и возвращает список словарей транзакций, сформированный по требованиям пользователя"""

    answers = []
    answers = get_variant(file_name)

    if answers[0] == '1':
        fn = f'{file_name}.json'
        try:
            #operations_data = json.load(open(fn, "r", encoding="UTF-8"))
            operations_data = json.load(open(fn, "r"))
        except FileNotFoundError, FileNotFoundError:
            print(f'Ошибка файла: {fn}')
            return answers[1], []

    elif answers[0] == '2':
        fn = f'{file_name}.csv'
        try:
            operations_data = read_csv(fn)
        except FileNotFoundError, FileNotFoundError:
            print(f'Ошибка файла: {fn}')
            return answers[1], []

    else:
        fn = f'{file_name}.xlsx'
        try:
            operations_data = read_xls(fn)
        except FileNotFoundError, FileNotFoundError:
            print(f'Ошибка файла: {fn}')
            return answers[1], []

    result_list=[operation for operation in operations_data if operation['state'] in answers[1]]

    if answers[3].lower() == 'по возрастанию':
        result_list.sort(key=itemgetter('date'))
    elif answers[3].lower() == 'по убыванию':
        result_list.sort(key=itemgetter('date'), reverse=True)

    if answers[4].lower() == 'да':
        result_list_rub = [trans_dict for trans_dict in result_list if trans_dict['currency_code'] == 'RUB']
        result_list = result_list_rub

    if answers[5].lower() == 'да':
        # answer_7 = input('Введите слово для поиска\n>>>')
        result_list = process_bank_search(result_list, state=answers[6])

    result_list

    return answers[1], result_list



def print_select(result_list: list[dict], state_select: str) -> None:
    """Функция вывода в консоль результатов выборки транзакций. Принимает подготовленный список словарей транзакций
    и строку заданных категорий состояния """

    print(f'Всего банковских операций в выборке: {len(result_list)}')
    print('Распечатываю итоговый список транзакций...\n')
    if len(result_list) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        for operation in result_list:
            print(f'{pd.to_datetime(operation['date']):%d.%m.%Y} {operation['description']}')
            try:
               empty_from = len(operation['from'])
            except TypeError:
                print(f'{mask_account_card(operation['to'])}')
            else:
                if empty_from > 0:
                    print(f'{mask_account_card(operation['from'])} -> {mask_account_card(operation['to'])}')
                else:
                    print(f'{mask_account_card(operation['to'])}')
            print(f'Сумма: {int(operation['amount'])} {operation["currency_code"]}\n')

    print(f'Банковские операции по выбранным категориям: {process_bank_operations(result_list, state_select)}')

def get_variant(file_name: str) -> list:
    """ Функция опроса пользователя и получения параметров обработки танзакций"""

    selection = {'1': 'JSON-файла', '2': 'CSV-файла', '3': 'XLSX-файла'}
    if file_name == '':
        file_name = 'data/test_transactions'
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        answer_1 = input("""\nВыберите необходимый пункт меню:\n
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла\n>>>""")
        if answer_1 not in ('1', '2', '3'):
            if answer_1 in ('q', 'quit'):
                break
            else:
                print('Вы ошиблись при выборе источника. Повторите ещё раз или нажмите "q" для выхода')
                continue
        else:
            print(f'Вы выбрали получение информации из {selection[answer_1]}\n')
            break

    while True:
        result_list = []
        all_available = True
        print('\nВведите статус, по которому необходимо выполнить фильтрацию.\n')
        answer_2 = input('Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n>>>')
        answer_2_list = re.split(r'[,\s]+', answer_2)
        for answer_2_element in answer_2_list:
            if answer_2_element.upper() not in ('EXECUTED', 'CANCELED', 'PENDING'):
                all_available = False
                print(f'Статус операции "{answer_2_element}" недоступен.')
        if all_available:
            break
    print(f'Операции отфильтрованы по статусу "{answer_2.upper()}"')

    answer_3 = input('Отсортировать операции по дате? Да/\033[1;4mНет\033[0m\n>>>')
    answer_4 = ''
    if answer_3.lower() == 'да':
               answer_4 = input('Отсортировать по возрастанию или по убыванию? \033[1;4mпо возрастанию\033[0m/по '
                         'убыванию\n>>>')

    answer_5 = input('Выводить только рублевые транзакции? Да/\033[1;4mНет\033[0m\n>>>')

    answer_6 = input('Отфильтровать список транзакций по определенному слову в описании? Да/\033[1;4mНет\033[0m\n>>>')

    answer_7 = ''
    if answer_6.lower() == 'да':
       answer_7 = input('Введите слово для поиска\n>>>')

    return [answer_1, answer_2_list, answer_3, answer_4, answer_5, answer_6, answer_7]

