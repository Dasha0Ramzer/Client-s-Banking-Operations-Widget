from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_number) != 16 or not card_number.isdigit():
        return "Некорректный номер карты"
    number_card_with_mask = f"{card_number[:6]}******{card_number[-4:]}"
    number_card_with_mask_result = ""
    for i in range(len(number_card_with_mask)):
        if i % 4 == 0 and i != 0:
            number_card_with_mask_result += " "
        number_card_with_mask_result += number_card_with_mask[i]
    return number_card_with_mask_result


def get_mask_account(account_number: Any) -> Any:
    """Функция маскировки номера банковского счета"""
    if len(account_number) != 20 or not account_number.isdigit():
        return "Некорректный номер счета"
    return "**" + account_number[-4:]
