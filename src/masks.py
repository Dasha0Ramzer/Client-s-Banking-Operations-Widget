import logging
from typing import Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    filename="./logs/masks.log",
    filemode="w",
)
masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler("./logs/masks.log")
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: Any) -> str:
    """Функция маскировки номера банковской карты"""

    masks_logger.debug("Проверяем на корректность введенного номера карты")
    if len(card_number) != 16 or not card_number.isdigit():

        masks_logger.error("Введен некорректный номер карты")
        return "Некорректный номер карты"

    masks_logger.debug('Маскируем часть номера карты, заменяя на символ "*"')
    number_card_with_mask = f"{card_number[:6]}******{card_number[-4:]}"
    number_card_with_mask_result = ""

    masks_logger.debug("Расставляем пробелы через каждые 4 цифры")
    for i in range(len(number_card_with_mask)):
        if i % 4 == 0 and i != 0:
            number_card_with_mask_result += " "
        number_card_with_mask_result += number_card_with_mask[i]

    masks_logger.info("Функция выполнена успешно")
    return number_card_with_mask_result


def get_mask_account(account_number: Any) -> Any:
    """Функция маскировки номера банковского счета"""

    masks_logger.debug("Проверяем на корректность введенного номера счета")
    if len(account_number) != 20 or not account_number.isdigit():

        masks_logger.error("Введен некорректный номер счета")
        return "Некорректный номер счета"

    masks_logger.debug("Маскируем номер счета")
    masks_logger.info("Функция выполнена успешно")
    return "**" + account_number[-4:]
