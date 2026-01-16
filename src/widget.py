from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_information: str) -> str:
    """Функция, маскирующая данные счета"""
    number = ""
    card_or_account = ""
    for symbol in account_information:
        if isinstance(symbol, int):
            break
        if symbol.isalpha() or symbol == " ":
            card_or_account += symbol
        else:
            number += symbol
    if len(number) == 20:
        return card_or_account + get_mask_account(number)  # Функция из masks.py
    elif len(number) == 16:
        return card_or_account + get_mask_card_number(number)  # Функция из masks.py
    else:
        return "Некорректный номер карты/счета"


def get_date(date_another_format: str) -> str:
    """Функция, возвращающая корректный формат даты"""
    if len(date_another_format) != 26:
        return 'Некорректные данные'
    day, month, year = "", "", ""
    year = date_another_format[:4]
    month = date_another_format[5:7]
    day = date_another_format[8:10]
    if not day.isdigit() and not month.isdigit() and not year.isdigit():
        return 'Некорректные данные'
    if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1 <= int(year) <= 2026:
        return f"{day}.{month}.{year}"
    else:
        return 'Такой даты не существует'
