import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s -  %(levelname)s - %(message)s")
file_path = f"logs/{__name__}.log"
file_handler = logging.FileHandler(file_path, encoding="utf-8", mode="w")
# file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""

    logger.info("Обработка номера карты")

    if len(card_number) == 16 and card_number.isdigit():
        mask_result = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Успешно. Выполнено маскирование карты: {card_number} с результатом: {mask_result}")
        return mask_result
    else:
        logger.error(f"Ошибка. Неверный номер карты: {card_number}")
        return ""


def get_mask_account(card_account: str) -> str:
    """принимает на вход номер карты и возвращает её краткую маску"""

    logger.info("Обработка номера карты")

    if len(card_account) == 20 and card_account.isdigit():
        mask_result = f"**{card_account[-4:]}"
        logger.info(f"Успешно. Выполнено маскирование карты: {card_account} с результатом: {mask_result}")
        return mask_result
    else:
        logger.error(f"Ошибка. Неверный номер карты: {card_account}")
        return ""
