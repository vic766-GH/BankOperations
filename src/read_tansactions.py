import csv
import pandas as pd

def read_csv(path_csv_file: str) -> list[dict]:
    """Функция чтения финансовых операций из файла типа 'csv'. В качестве аргумента принимает путь к файлу и возвращает
    список словарей прочитанных транзакций"""
    with open(path_csv_file, encoding='UTF-8') as file:
        transactions = csv.DictReader(file, delimiter=';')
        #transactions = pd.read_csv(file, delimiter=';')
        list_transactions = list(transactions)
    return list_transactions

def read_xls(path_xls_file: str) -> list[dict]:
    """Функция чтения финансовых операций из файла типа 'Excel'. В качестве аргумента принимает путь к файлу и
    возвращает список словарей прочитанных транзакций"""
    #with open(path_xls_file, encoding='UTF-8') as file:
    #with open(path_xls_file) as file:
    transactions = pd.read_excel(path_xls_file)
    list_transactions = transactions.to_dict(orient='records')
    return list_transactions

def main():
    """ Функция производит вызов функций для чтения финансовых операций из файлов типа 'csv' и 'Excel'. Выводит в
    консоль информацию о количестве прочитанных транзакций """
    csv_file_name = 'transactions.csv'
    transactions_in_csv = read_csv(f'..\\data\\{csv_file_name}')
    print(f'Количество транзакций в файле "{csv_file_name}":{len(transactions_in_csv)}')
    # row = 1
    # for dict_transaction in transactions_in_csv:
    #     print(f'Транзакция {row}: {dict_transaction.keys()}: {dict_transaction.values()}')
    #     row += 1
    #     for k, v in dict_transaction.items():
    #         print(f'{k}:{v}')

    excel_file_name = 'transactions_excel.xlsx'
    transactions_in_xls = read_xls(f'..\\data\\{excel_file_name}')
    print(f'Количество транзакций в файле "{excel_file_name}":{len(transactions_in_xls)}')
    # row = 1
    # for dict_transaction in transactions_in_xls:
    #     print(f'Транзакция {row}: {dict_transaction.keys()}: {dict_transaction.values()}')
    #     row += 1
    #     for k, v in dict_transaction.items():
    #         print(f'{k}:{v}')


if __name__ == '__main__':
    main()
    # Количество транзакций в файле "transactions.csv": 1000
    # Количество транзакций в файле "transactions_excel.xlsx": 1000