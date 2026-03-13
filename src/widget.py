from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Принимает информацию о карте или счёте. Возвращает замаскированную строку"""

    first_space_index = card_info.find(" ")
    last_space_index = card_info.rfind(" ")

    if len(card_info) == 0:
        return ""
    if card_info[:first_space_index] == "Счет":
        if len(card_info) ==25:
            return f"Счет {get_mask_account(card_info[first_space_index + 1:])}"
        elif len(card_info) > 24: # Некорректные данные - превышено количество цифр в счёте карты
            return ""
        elif len(card_info) < 25: # Некорректные данные - недостаточно цифр в счёте карты или отсутствует счёт карты
            return ""
        else:
#            return f"Счет {get_mask_account(card_info[first_space_index + 1:])}"
            return "OK???"
    else:
        if not len(card_info[last_space_index + 1:]) == 16:
            return ""
        elif len(card_info) <= 16: # Некорректные данные - отсутствует наименование или номер карты, или ключевое слово
            return ""
        elif len(card_info[last_space_index + 1:]) > 16: # Некорректные данные - превышено количество цифр в номере карты
            return ""
        elif len(card_info[last_space_index + 1:]) < 16: # Некорректные данные - недостаточно цифр в номере карты
            return ""
        elif not card_info[last_space_index + 1:].isdigit():
            return ""
        else:
            return f"{card_info[: last_space_index]} {get_mask_card_number(card_info[last_space_index + 1:])}"



def get_date(date_string: str) -> str:
    """ Принимает строку с текущей датой и возвращает строку в формате 'ДД.ММ.ГГГГ'"""

    return f"{date_string[8:10]}.{date_string[5: 7]}.{date_string[: 4]}"
