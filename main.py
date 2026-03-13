# Это пример Python скрипта.


# Нажмите Shift+F10 для выполнения или замените его своим кодом.
# Нажмите Двойное нажатие Shift для поиска везде: классы, файлы, окна инструментов, действия и настройки.
# def print_hi(name):
# Используйте точку останова в строке кода ниже для отладки скрипта.
#     print(f"Hi, {name}")  # Нажмите Ctrl+F8 для переключения точки останова.


# Нажмите зеленую кнопку на полях для запуска скрипта.

#    print_hi("PyCharm")

# Справка PyCharm доступна на https://www.jetbrains.com/help/pycharm/


# from src.masks import get_mask_card_number, get_mask_account

# print(get_mask_card_number('7000792289606361'))
# print(get_mask_account('73654108430135874305'))

from src.widget import mask_account_card, get_date

input_data = (
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
)
# from src.processing import filter_by_state, sort_by_date
#
# in_list_dict = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
# state = 'EXECUTED'
# sort_by_descending_order = False

if __name__ == "__main__":
    for input_string in input_data:
        print(mask_account_card(input_string))
    # print(get_date('2024-03-11T02:26:18.671407'))

#    print(sort_by_date(filter_by_state(in_list_dict, state), sort_by_descending_order))
