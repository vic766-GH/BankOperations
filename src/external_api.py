import os
from json import loads

import requests
import json

from unittest.mock import Mock
from unittest.mock import patch
from dotenv import load_dotenv


# Загрузка переменных из .env-файла
load_dotenv()

# APILAYER_ERROR_CODE = {
#     400:{"STATUS_CODE":"Bad Request",
#          "EXPLANATION":"The request was unacceptable,often due to missing a required parameter."},
#     401: {"STATUS_CODE" : "Unauthorized",
#           "EXPLANATION":"No valid API key provided."},
#     404: {"STATUS_CODE" : "Not Found",
#           "EXPLANATION":"The requested resource doesn't exist."},
#     429: {"STATUS_CODE" : "Too many requests",
#           "EXPLANATION":"API request limit exceeded. See section Rate Limiting for more info."},
#     500: {"STATUS_CODE" : "Server Error",
#           "EXPLANATION":"We have failed to process your request. (You can contact us anytime)"}
# }

def convert_currency(date: str, to_currency: str, from_currency: str, amount: str) -> float:
    """Получает информацию о транзакции и возвращает сумму транзакции в целевой валюте после конвертации
    исходной валюты по курсу на заданную дату с использованием сервиса APILayer"""

    headers = {"apikey": os.getenv('APILAYER_KEY')}
    url_convert = (f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}"
                   f"&amount={amount}&date={date}")

    converted = requests.get(url_convert, headers=headers)
    converted_type = type(converted)
    if converted_type != dict:
        converted_dict = loads(converted.text)
        if len(converted_dict) == 1:

            print(f"Ошибка: {converted_dict}")
            return 0
    else:
        converted_dict = converted
    # status_code = converted.status_code

    # if status_code == 200:
    #     converted_list = json.loads(converted.text)
    #     result = round(converted_dict["result"],2)
    #     return result
    # else:
    #     status = APILAYER_ERROR_CODE[status_code]["STATUS_CODE"]
    #     explanation = APILAYER_ERROR_CODE[status_code]["EXPLANATION"]
    #     print(f"Код возврата от сервера: {status_code}:{status} ({explanation})")
    #     return 0

    result = round(converted_dict["result"], 2)
    return result