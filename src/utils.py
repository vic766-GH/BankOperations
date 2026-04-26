import json
from external_api import convert_currency


def get_operations(path: str) -> list[dict]:

    """Функция получает путь к файлу с данными о транзакциях и возвращает список словарей с транзакциями"""

    try:
        with open(path,'r', encoding='UTF-8') as operations_file:
            try:
                operations_list = json.load(operations_file)
            except json.decoder.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []

    return operations_list

def transaction_tu_rub(transaction: dict) -> float:
    """Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    try:
        date_in = transaction['date'][0:10]
        amount_in = transaction['operationAmount']['amount']
        currency_in = transaction['operationAmount']['currency']['code']
    except KeyError:
        return 0
    except TypeError:
        return 0
    if currency_in == 'RUB':
        return float(amount_in)
    else:
        amount_out = convert_currency(date_in,'RUB',currency_in,amount_in)
        return amount_out
