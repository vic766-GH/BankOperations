import json
import re
import datetime
import collections
import pandas as pd
from collections import Counter
from operator import itemgetter
from src.widget import mask_account_card

from numpy.ma.core import append

import src.processing as processing

from src.utils import get_operations
from src.read_transactions import read_csv, read_xls



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


def main() -> None:
    """Основная функция взаимодействия с пользователем."""

    selection = {'1': 'JSON-файла','2': 'CSV-файла','3': 'XLSX-файла'}


    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        answer_1 = input("""\nВыберите необходимый пункт меню:\n
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла\n>>>""")
        if answer_1 not in ('1','2','3'):
            if answer_1 in ('q','quit'):
                break
            else:
                print('Вы ошиблись при выборе источника. Повторите ещё раз или нажмите "q" для выхода')
                continue
        else:
            print(f'Вы выбрали получение информации из {selection[answer_1]}\n')
            if answer_1 == '1':
                operations_data = json.load(open('data/transactions.json', "r", encoding="UTF-8"))
                break
            elif answer_1 == '2':
                operations_data = read_csv('data/transactions.csv')
                break
                # with open('data/transactions.json', 'w') as file:
                #     json.dump(operations_data, file)
            elif answer_1 == '3':
                operations_data = read_xls('data/transactions_excel.xlsx')
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
            else:
                result_list.extend(processing.filter_by_state(operations_data, state=answer_2_element.upper()))
        if all_available:
            break
    print(f'Операции отфильтрованы по статусу "{answer_2.upper()}"')

    answer_3 = input('Отсортировать операции по дате? Да/\033[1;4mНет\033[0m\n>>>')
    if answer_3.lower() == 'да':
        answer_4 = input('Отсортировать по возрастанию или по убыванию? \033[1;4mпо возрастанию\033[0m/по '
                         'убыванию\n>>>')
        if answer_4.lower() == 'по возрастанию':
            result_list.sort(key=itemgetter('date'))
        elif answer_4.lower() == 'по убыванию':
            result_list.sort(key=itemgetter('date'), reverse=True)

    answer_5 = input('Выводить только рублевые транзакции? Да/\033[1;4mНет\033[0m\n>>>')
    if answer_5.lower() == 'да':
        result_list_rub = [trans_dict for trans_dict in result_list if trans_dict['currency_code'] == 'RUB']
        result_list = result_list_rub


    answer_6 = input('Отфильтровать список транзакций по определенному слову в описании? Да/\033[1;4mНет\033[0m\n>>>')
    if answer_6.lower() == 'да':
        answer_7 = input('Введите слово для поиска\n>>>')
        result_list = process_bank_search(result_list, state=answer_7)

    print(f'Всего банковских операций в выборке: {len(result_list)}')
    patt_date = r'\d{4}-\d{2}-\d{2}'


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
            print(f'Сумма: {operation['amount']} {operation["currency_code"]}\n')

    #print(t'Банковские операции по выбранным категориям: {process_bank_operations(operations_data, answer_2_list)}')


if __name__ == '__main__':
    main()
