def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) > 0:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
    return ""

def get_mask_account(card_number: str) -> str:
    """принимает на вход номер карты и возвращает её краткую маску"""

    return f"**{card_number[-4:]}"
