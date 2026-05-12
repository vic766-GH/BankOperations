# import logging
#
# from utils import get_operations, transaction_to_rub
# from external_api import convert_currency
#
# def main():
#
#     logger = logging.getLogger("utils")
#
#     logger.info(f"Начало работы")
#     print(f"Начало работы")
#     path = "data/operations.json"
#     logger.info(f"Чтение транзакций из файла: {path}")
#     results = get_operations(path)
#     for result in results:
#         try:
#             transaction_date = result["date"][0:10]
#             transaction_amount = result["operationAmount"]["amount"]
#             transaction_currency = result["operationAmount"]["currency"]["code"]
# #            print(convert_currency(transaction_date, "RUB", transaction_currency, transaction_amount))
#         except KeyError:
#             logger.error(f"Ошибка в {results.index(result) + 1} словаре: {result}")
#     #        print(f"Ошибка в {results.index(result) + 1} словаре: {result}")
#     logger.info(f"Обработано {len(results)} транзакций")
#     #print(f"Обработано {len(results)} транзакций")
#
#     transactions = [
#             {
#                 "id": 441945886,
#                 "state": "EXECUTED",
#                 "date": "2019-08-26T10:50:58.294041",
#                 "operationAmount": {
#                     "amount": "31957.58",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Maestro 1596837868705199",
#                 "to": "Счет 64686473678894779589"
#             },
#             {
#                 "id": 41428829,
#                 "state": "EXECUTED",
#                 "date": "2019-07-03T18:35:29.512364",
#                 "operationAmount": {
#                     "amount": "8221.37",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "MasterCard 7158300734726758",
#                 "to": "Счет 35383033474447895560"
#             },
#             {
#                 "id": 41428829,
#                 "state": "EXECUTED",
#                 "date": "2019-07-03T18:35:29.512364",
#                 "operationAmount": {
#                     "amount": "8221.37",
#                     "currency": {
#                         "name": "EUR",
#                         "code": "EUR"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "MasterCard 7158300734726758",
#                 "to": "Счет 35383033474447895560"
#                 },
#             {}
#     ]
#     logger.info(f"Обработка списка транзакций из {len(transactions)} элементов")
#     for transaction in transactions:
#         logger.info(transaction_to_rub(transaction))
#
#     logger.info(f"Обработка некорректных транзакций")
#     transaction_date = "2019-12-07"
#     transaction_amount = "48150.39"
#     logger.info(f"{convert_currency(transaction_date, "RUB", "USD", transaction_amount)}\n")  # Корректные данные
#     logger.info(f"{convert_currency(transaction_date, "RUB", "USB",transaction_amount)}\n") # неверная валюта для конвертации
#     logger.info(f"{convert_currency(transaction_date, "SUB", "USB", transaction_amount)}\n") # неверная валюта в которую конвертируем
#     logger.info(f"{convert_currency(transaction_date, "SUB", "USB", transaction_amount)}\n") # неверная валюта в обоих случаях
#     logger.info(f"{convert_currency(transaction_date, "RUВ", "USD", transaction_amount)}\n")  # неверная валюта в которую
#     # конвертируем - использован символ в русской раскладке
#     transaction_date = "2019-14-07"
#     logger.info(f"{convert_currency(transaction_date, "RUB", "USD", transaction_amount)}\n") # неверная дата - ошибка в месяце
#     transaction_date = "2019-12-07"
#     transaction_amount = "4815O.39"
#     logger.info(f"{convert_currency(transaction_date, "RUB", "USD", transaction_amount)}\n")  # неверное количество для
#     # конвертации - вместо 0 присутствует
#     logger.info(f"Обработка завершена\n")
#     print(f"Обработка завершена\n")
#     # print(f"{convert_currency(transaction_date, "RUB", "USD", transaction_amount)}\n")  # Корректные данные
#     # print(f"{convert_currency(transaction_date, "RUB", "USB",transaction_amount)}\n") # неверная валюта для конвертации
#     # print(f"{convert_currency(transaction_date, "SUB", "USB", transaction_amount)}\n") # неверная валюта в которую конвертируем
#     # print(f"{convert_currency(transaction_date, "SUB", "USB", transaction_amount)}\n") # неверная валюта в обоих случаях
#     # print(f"{convert_currency(transaction_date, "RUВ", "USD", transaction_amount)}\n")  # неверная валюта в которую
#     # # конвертируем - использован символ в русской раскладке
#     # transaction_date = "2019-14-07"
#     # print(f"{convert_currency(transaction_date, "RUB", "USD", transaction_amount)}\n") # неверная дата - ошибка в месяце
#     # transaction_date = "2019-12-07"
#     # transaction_amount = "4815O.39"
#     # print(f"{convert_currency(transaction_date, "RUB", "USD", transaction_amount)}\n")  # неверное количество для
#     # # конвертации - вместо 0 присутствует
#
# if __name__ == "__main__":
#     main()