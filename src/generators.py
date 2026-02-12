from typing import Any, Iterator


def filter_by_currency(transactions: Any, currency: Any) -> Any:
    """Функция, выдающая транзакции, где валюта операции соответствует заданной"""
    if not isinstance(transactions, list):
        raise TypeError("transactions must be a list")
    if len(transactions) == 0:
        return "Список транзакций пуст"
    result = (
        dict_
        for dict_ in transactions
        if "operationAmount" in dict_
        and dict_["operationAmount"]["currency"]["code"] == currency
        or "currency_code" in dict_
        and dict_["currency_code"] == currency
    )
    return result


def transaction_descriptions(transaction: Any) -> Iterator[str]:
    """Функция, возвращающая описание каждой транзакции"""
    if not transaction:
        yield "Список транзакций пуст"
    for dict_ in transaction:
        yield dict_["description"]


def card_number_generator(start: Any, stop: Any) -> Iterator[str]:
    """Функция, генерирующая номера банковских карт"""
    for number in range(start, stop + 1):
        if len(str(number)) < 16:
            full_card_number = str(number).rjust(16, "0")
            result = ""
            for i in range(len(full_card_number)):
                if i % 4 == 0 and i != 0:
                    result += " "
                result += full_card_number[i]
            yield result
        else:
            yield "Это уже не номер карты, проверьте введенные данные"
