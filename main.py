import pandas as pd
import json
import os
import inspect

from pathlib import Path
from src.trans_operations import source_select, print_select


def main() -> None:
    """Основная функция для вызова вспомогательных модулей взаимодействия с пользователем и вывода в консоль
    результатов выборки транзакций"""

    source_file = "transactions"
    # source_file = 'test_transactions'
    # source_file = ''

    # Вызываем функцию выбора файла-источника транзакций
    state_select, result_list = source_select(source_file)

    # Вызываем функцию печати выбранных транзакций
    print_select(result_list, state_select)

# создание копий (JSON, XLXS) файла CSV
# def convert_file() -> None:
#     """Функция конвертирования файлов"""
#
#     pd_data = pd.read_csv('data/test_transactions.csv',sep=';')
#     #pd_data = pd.read_excel('data/test_transactions.xlxs', index_col=0)
#     #pd_data.to_csv('data/test_transactions.csv')
#     print(pd_data)
#     pd1_data = pd_data.to_dict(orient='records')
#     print(pd1_data)
#     json.dump(pd1_data, open('data/test_transactions.json', 'w', encoding='UTF-8'), indent=4, ensure_ascii=True,
#               sort_keys=False)
#     #pd.DataFrame(pd_data).to_excel('data/test_transactions.xlsx', index=False)
#     pd.DataFrame(pd_data).to_json('data/test_transactions.json', indent=4, orient='records',index=False)


if __name__ == '__main__':
    #convert_file()
    main()
