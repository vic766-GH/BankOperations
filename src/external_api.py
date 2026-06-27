import json
import logging
import os
from json import loads

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

logger = logging.getLogger("utils")

APILAYER_ERROR_CODE = {
    400: {
        "STATUS_CODE": "Bad Request",
        "EXPLANATION": "The request was unacceptable,often due to missing a required parameter.",
    },
    401: {"STATUS_CODE": "Unauthorized", "EXPLANATION": "No valid API key provided."},
    404: {
        "STATUS_CODE": "Not Found",
        "EXPLANATION": "The requested resource doesn't exist.",
    },
    429: {
        "STATUS_CODE": "Too many requests",
        "EXPLANATION": "API request limit exceeded. See section Rate Limiting for more info.",
    },
    500: {
        "STATUS_CODE": "Server Error",
        "EXPLANATION": "We have failed to process your request. (You can contact us anytime)",
    },
}


def convert_currency(
    date: str, to_currency: str, from_currency: str, amount: str
) -> float:
    """Получает информацию о транзакции и возвращает сумму транзакции в целевой валюте после конвертации
    исходной валюты по курсу на заданную дату с использованием сервиса APILayer"""

    url_convert = (
        f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}"
        f"&amount={amount}&date={date}"
    )
    payload: dict = {}
    apikey = {"apikey": str(os.getenv("APILAYER_KEY"))}

    logger.info(f"Обращение к внешнему API: {url_convert[0:24]}")
    converted = requests.request("GET", url=url_convert, headers=apikey, data=payload)
    status_code = converted.status_code
    if status_code == 200:
        converted_list = json.loads(converted.text)
        result: float = round(converted_list["result"], 2)
        return result
    else:
        status = APILAYER_ERROR_CODE[status_code]["STATUS_CODE"]
        explanation = APILAYER_ERROR_CODE[status_code]["EXPLANATION"]
        error_code = loads(converted.content)
        logger.error(f"Код возврата от сервера: {status_code}:{status} ({explanation})")
        # print(f"Код возврата от сервера: {status_code}:{status} ({explanation})")
        try:
            logger.error(
                f"{error_code["error"]["code"]} ({error_code["error"]["message"]}"
            )
        #    print(f"{error_code["error"]["code"]} ({error_code["error"]["message"]}")
        except KeyError:
            logger.error(f"{error_code["message"]}")
        #    print(f"{error_code["message"]}")
        return 0
