from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_information: str) -> str:
    """Функция, маскирующая данные счета"""
    number = ""
    card_or_account = ""
    for symbol in account_information:
        if symbol.isalpha() or symbol == " ":
            card_or_account += symbol
        else:
            number += symbol
    if card_or_account == "Счет ":
        return card_or_account + get_mask_account(number)  # Функция из masks.py
    else:
        return card_or_account + get_mask_card_number(number)  # Функция из masks.py


def get_date(date_another_format: str) -> str:
    """Функция, возвращающая корректный формат даты"""
    day, month, year = "", "", ""
    year = date_another_format[:4]
    month = date_another_format[5:7]
    day = date_another_format[8:10]
    return f"{day}.{month}.{year}"
