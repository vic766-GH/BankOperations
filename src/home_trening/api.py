import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()


"""
Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
тип данных — float. Если транзакция была в USD или EUR,
происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли.
Для конвертации валюты воспользуйтесь Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
Функцию конвертации поместите в модуль external_api.
для сокрытия чувствительных данных (токенов доступа для API). Создайте шаблон файла 111.env
Напишите тесты для новых функций, используйте Mock и patch.
"""


def get_convert(transaction: Dict) -> float:
    currency_code = transaction.get("operationAmount").get("currency").get("code")
    amount = transaction.get("operationAmount").get("amount")
    if currency_code == "RUB":
        return float(amount)

    elif currency_code in ["USD", "EUR"]:

        data = {"from": currency_code, "to": "RUB", "amount": amount}

        url = os.getenv("URL")
        headers = {"apikey": os.getenv("API")}

        try:
            response = requests.get(url, headers=headers, data=data)
            print(response.json())
            return float(response.json().get("result"))
        except Exception as e:
            print(str(e))


transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "310.50", "currency": {"name": "руб.", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

get_convert(transaction)
