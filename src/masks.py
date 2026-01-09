def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    number_card_with_mask = f'{card_number[:6]}******{card_number[-4:]}'
    number_card_with_mask_result = ""
    for i in range(len(number_card_with_mask)):
        if i % 4 == 0:
            number_card_with_mask_result += " "
        number_card_with_mask_result += number_card_with_mask[i]
    return number_card_with_mask_result


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    return "**" + account_number[-4:]
