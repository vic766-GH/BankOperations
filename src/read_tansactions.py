import csv
import os

import pandas as pd


def read_csv(path_csv_file: str) -> list[dict]:
    """Функция чтения финансовых операций из файла типа 'csv'. В качестве аргумента принимает путь к файлу и возвращает
    список словарей прочитанных транзакций"""
    with open(path_csv_file, encoding="UTF-8") as file:
        csv_transactions = csv.DictReader(file, delimiter=";")
        list_transactions = list(csv_transactions)
    return list_transactions


def read_xls(path_xls_file: str) -> list[dict]:
    """Функция чтения финансовых операций из файла типа 'Excel'. В качестве аргумента принимает путь к файлу и
    возвращает список словарей прочитанных транзакций
    :rtype: list[dict]"""

    xlx_transactions = pd.read_excel(path_xls_file)
    list_transactions = list(xlx_transactions.to_dict(orient="records"))

    return list_transactions


def main() -> None:
    """Функция производит вызов функций для чтения финансовых операций из файлов типа 'csv' и 'Excel'. Выводит в
    консоль информацию о количестве прочитанных транзакций"""

    # Количество транзакций в файле "transactions.csv": 1000
    # Количество транзакций в файле "transactions_excel.xlsx": 1000

    csv_file_name = "transactions.csv"
    current_directory = os.getcwd()
    path_csv_file = f"{current_directory}\\..\\data\\{csv_file_name}"
    transactions_in_csv = read_csv(path_csv_file)
    print(f'Количество транзакций в файле "{csv_file_name}":{len(transactions_in_csv)}')

    excel_file_name = "transactions_excel.xlsx"
    transactions_in_xls = read_xls(f"..\\data\\{excel_file_name}")
    print(f'Количество транзакций в файле "{excel_file_name}":{len(transactions_in_xls)}')


if __name__ == "__main__":
    main()
