from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Принимает информацию о карте или счёте. Возвращает замаскированную строку"""

    first_space_index = card_info.find(" ")
    last_space_index = card_info.rfind(" ")

    if card_info[:first_space_index] == "Счет":
        return f"Счет {get_mask_account(card_info[first_space_index + 1:])}"
    else:
        if first_space_index == last_space_index:
            return f"{card_info[: first_space_index]} {get_mask_card_number(card_info[first_space_index + 1:])}"
        else:
            return f"{card_info[: last_space_index]} {get_mask_card_number(card_info[last_space_index + 1:])}"
