import csv
from pathlib import Path

import pandas as pd


def read_csv(path_csv_file: str) -> list[dict]:
    """Функция чтения финансовых операций из файла типа 'csv'. В качестве аргумента принимает путь к файлу в виде
    строки и возвращает список словарей прочитанных транзакций"""
    with open(path_csv_file, encoding="UTF-8") as file:
        csv_transactions = csv.DictReader(file, delimiter=";")
        list_transactions = list(csv_transactions)
    return list_transactions


def read_xls(path_xls_file: str) -> list[dict]:
    """Функция чтения финансовых операций из файла типа 'Excel'. В качестве аргумента принимает путь к файлу в виде
    строки и возвращает список словарей прочитанных транзакций"""

    xlx_transactions = pd.read_excel(path_xls_file)
    list_transactions = list(xlx_transactions.to_dict(orient="records"))

    return list_transactions


def main() -> None:
    """Функция производит вызов функций для чтения финансовых операций из файлов типа 'csv' и 'Excel'. Выводит в
    консоль информацию о количестве прочитанных транзакций"""

    # Количество транзакций в файле "transactions.csv": 1000
    # Количество транзакций в файле "transactions_excel.xlsx": 1000

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent
    csv_file_name = "transactions.csv"
    relative_path = Path(f"{BASE_DIR}/../data/{csv_file_name}")
    absolute_path = relative_path.resolve()  # Преобразует путь в абсолютный
    path_csv_file = absolute_path
    transactions_in_csv = read_csv(str(path_csv_file))
    print(f'Количество транзакций в файле "{csv_file_name}":{len(transactions_in_csv)}')

    excel_file_name = "transactions_excel.xlsx"
    relative_path = Path(f"{BASE_DIR}/../data/{excel_file_name}")
    absolute_path = relative_path.resolve()  # Преобразует путь в абсолютный
    path_excel_file = absolute_path
    transactions_in_xls = read_xls(str(path_excel_file))
    print(f'Количество транзакций в файле "{excel_file_name}":{len(transactions_in_xls)}')


if __name__ == "__main__":
    main()
