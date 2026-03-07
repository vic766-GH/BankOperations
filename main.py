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

if __name__ == "__main__":
    for input_string in input_data:
        print(mask_account_card(input_string))
    print(get_date('2024-03-11T02:26:18.671407'))
