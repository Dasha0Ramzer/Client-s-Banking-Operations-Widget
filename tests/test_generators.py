from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
        ("123", []),
        ([1, 2], []),
    ],
)
def test_filter_by_currency(transactions: list[dict], currency: Any, expected: Any) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


def test_filter_by_currency_empty() -> None:
    result = filter_by_currency([], "USD")
    assert result == "Список транзакций пуст"


def test_filter_by_currency_type_error2() -> None:
    with pytest.raises(TypeError):
        filter_by_currency("", "USD")


def test_filter_by_currency_type_error3() -> None:
    with pytest.raises(TypeError):
        filter_by_currency(123, "USD")


def test_filter_by_currency_with_key_error(transactions2: list[dict]) -> None:
    with pytest.raises(KeyError):
        list(filter_by_currency(transactions2, "USD"))
    with pytest.raises(KeyError):
        list(filter_by_currency(transactions2, "RUB"))


def test_transaction_descriptions(transactions: list[dict]) -> None:
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"


def test_transaction_descriptions_empty1() -> None:
    generator = transaction_descriptions([])
    assert next(generator) == "Список транзакций пуст"


def test_transaction_descriptions_empty2() -> None:
    generator = transaction_descriptions("")
    assert next(generator) == "Список транзакций пуст"


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (5, 7, ["0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007"]),
        (9999999999999999, 9999999999999999999, ["Это уже не номер карты, проверьте введенные данные"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: list) -> None:
    generator = card_number_generator(start, end)
    for exp in expected:
        assert next(generator) == exp


def test_card_number_generator_type_error1() -> None:
    generator = card_number_generator("123", "234")
    with pytest.raises(TypeError):
        next(generator)


def test_card_number_generator_type_error2() -> None:
    generator = card_number_generator(123, "234")
    with pytest.raises(TypeError):
        next(generator)
