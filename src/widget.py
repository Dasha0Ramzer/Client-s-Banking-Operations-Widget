import masks


def mask_account_card(account_information: str) -> str:
    """Функция, маскирующая данные счета"""
    number = ''
    card_or_account = ''
    for symbol in account_information:
        if symbol.isalpha() or symbol == ' ':
            card_or_account += symbol
        else:
            number += symbol
    if card_or_account == 'Счет ':
        return card_or_account + masks.get_mask_account(number)
    else:
        return card_or_account + masks.get_mask_card_number(number)


def get_date(date_another_format: str) -> str:
    """Функция, возвращающая корректный формат даты"""
    day, month, year = '', '', ''
    year = date_another_format[:4]
    month = date_another_format[5:7]
    day = date_another_format[8:10]
    return f'{day}.{month}.{year}'