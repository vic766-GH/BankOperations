def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""

    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return ""


def get_mask_account(card_account: str) -> str:
    """принимает на вход номер карты и возвращает её краткую маску"""

    if len(card_account) == 20 and card_account.isdigit():
        return f"**{card_account[-4:]}"
    else:
        return ""
