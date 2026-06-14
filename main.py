from src.trans_operations import source_select, print_select, process_bank_operations

def main() -> None:
    """Основная функция взаимодействия с пользователем."""

    #source_file = 'data/transactions'
    source_file = 'data/test_transactions'
    #source_file = ''

# Вызываем функцию выбора файла-источника транзакций
    result_list, state_select = source_select(source_file)

# Вызываем функцию печати выбранных транзакций
    print_select(result_list, state_select)



# создание копий (JSON, XLXS) файла CSV
#import pandas as pd
#
#def convert_file() -> None:
#    pd_csv = pd.read_csv('data/test_transactions.csv')
#    print(pd_csv)
#    pd.DataFrame(pd_csv).to_excel('data/test_transactions.xlsx', index=False)
#    pd.DataFrame(pd_csv).to_json('data/test_transactions.json', indent=4, orient='records', index=False)




if __name__ == '__main__':
    # convert_file()
    main()
