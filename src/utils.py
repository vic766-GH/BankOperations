import json
import logging

from src.external_api import convert_currency

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s -  %(levelname)s - %(message)s')
file_path = f"logs/{__name__}.log"
file_handler = logging.FileHandler(file_path, encoding="utf-8", mode="w")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_operations(path: str) -> list:
    """Функция получает путь к файлу с данными о транзакциях и возвращает список словарей с транзакциями"""

    try:
        with open(path, "r", encoding="UTF-8") as operations_file:
            try:
                logger.info(f"Получение транзакций из файла: {path}")
                operations_list: list = json.load(operations_file)
                logger.info(f"Транзакции получены успешно")
            # except json.decoder.JSONDecodeError:
            except Exception as e:
                # print("Ошибка декодирования файла")
                logger.error(f"Ошибка получения транзакций из файла: {e}")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []

    return operations_list


def transaction_to_rub(transaction: dict) -> float:
    """Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    try:
        logger.info(f"Начало обработки транзакции")
        date_in = transaction["date"][0:10]
        amount_in = transaction["operationAmount"]["amount"]
        currency_in = transaction["operationAmount"]["currency"]["code"]
    except KeyError:
        logger.error(f"Ошибка ключа словаря")
        return 0
    except TypeError:
        logger.error(f"Ошибка типа")
        return 0
    if currency_in == "RUB":
        logger.info(f"Рублёвая транзакция")
        return float(amount_in)
    else:
        logger.info(f"Конвертация валюты по транзакции")
        amount_out = float(convert_currency(date_in, "RUB", currency_in, amount_in))
        return amount_out
