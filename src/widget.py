from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Принимает информацию о карте или счёте. Возвращает замаскированную строку"""

    first_space_index = card_info.find(" ")
    last_space_index = card_info.rfind(" ")

    card_info_number = card_info[last_space_index + 1 :]
    len_card_info_number = len(card_info_number)

    if len(card_info) == 0:  # Проверка пустой строки
        print("Некорректные данные - Пустая строка")
        return ""
    if len(card_info) <= 16:  # Некорректные данные - отсутствует наименование или номер карты, или ключевое слово
        print("Некорректные данные - отсутствует наименование или номер карты, номер счёта, или ключевое слово")
        return ""
    if not card_info_number.isdigit():  # Проверка на наличие не цифровых символов в номере
        print("Некорректные данные - наличие не цифровых символов в номере")
        return ""

    # Обработка Счёта
    if card_info[:first_space_index] == "Счет":
        if len_card_info_number == 20:
            print("Корректный счёт")
            return f"Счет {get_mask_account(card_info_number)}"
        elif len_card_info_number > 20:  # Некорректные данные - превышено количество цифр в счёте
            print("Некорректные данные - превышено количество цифр в счёте")
            return ""
        else:
            # Некорректные данные - недостаточно цифр в счёте карты или отсутствует счёт карты
            print("Некорректные данные - недостаточно цифр в счёте или отсутствует счёт")
            return ""
    # Обработка Карты
    else:
        if len_card_info_number == 20:
            print("Некорректные данные - ошибка в ключевом слове")
            return ""
        elif len_card_info_number == 16:
            print("Корректная карта")
            return f"{card_info[: last_space_index]} {get_mask_card_number(card_info_number)}"
        elif len(card_info_number) > 16:  # Некорректные данные - превышено количество цифр в номере карты
            print("Некорректные данные - превышено количество цифр в номере карты")
            return ""
        else:
            # Некорректные данные - недостаточно цифр в номере карты
            print("Некорректные данные - недостаточно цифр в номере карты")
            return ""


def get_date(date_string: str) -> str:
    """Принимает строку с текущей датой и возвращает строку в формате 'ДД.ММ.ГГГГ'"""

    if len(date_string) == 0:  # Пустая строка
        return ""
    elif len(date_string) > 26:  # Длинная строка
        return ""
    else:
        if 1 <= int(date_string[5:7]) <= 12:  # Месяц внутри допустимого диапазона
            if 1 <= int(date_string[8:10]) <= 31:  # День внутри допустимого диапазона
                return f"{date_string[8:10]}.{date_string[5: 7]}.{date_string[: 4]}"
            else:
                return ""
        else:
            return ""
