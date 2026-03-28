from typing import Any, Generator


def filter_by_currency(list_of_dicts: list, currency: str) -> Generator[dict, None, None]:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    filtered_list = filter(
        lambda dict_in_list: dict_in_list["operationAmount"].get("currency").get("code") == currency, list_of_dicts
    )
    for dictionary in filtered_list:
        yield dictionary


def transaction_descriptions(list_of_dicts: list) -> Generator[str, None, None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for dictionary in list_of_dicts:
        yield dictionary["description"]


def card_number_generator(first_num: int, last_num: int) -> Generator[str, None, Any]:
    """Функция принимает начальное и конечное значения и выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001
    до 9999 9999 9999 9999"""

    i = first_num

    if first_num >= last_num:
        return []

    while i <= last_num:
        string_out = f"{str(i):>016}"
        string_out = f"{string_out[:4]} {string_out[4:8]} {string_out[8:12]} {string_out[12:]}"
        i += 1
        yield string_out
