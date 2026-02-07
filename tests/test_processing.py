from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("None", "Данный статус отсутствует"),
        ([1, 2, 3, 4], "Данный статус отсутствует"),
        (1234, "Данный статус отсутствует"),
    ],
)
def test_filter_by_state(list_dicts: list[dict], state: Any, expected: Any) -> None:
    assert filter_by_state(list_dicts, state) == expected


@pytest.mark.parametrize(
    "list_of_dictionaries, expected",
    [([], "Операции отсутствуют"), ("", "Некорректные данные"), (["aaa", 2], "Некорректные данные")],
)
def test_filter_by_state_with_type_error(list_of_dictionaries: Any, expected: str) -> None:
    assert filter_by_state(list_of_dictionaries) == expected


@pytest.mark.parametrize(
    "reversed, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(list_dicts: list[dict], reversed: bool, expected: list[dict]) -> None:
    assert sort_by_date(list_dicts, reversed) == expected


@pytest.mark.parametrize(
    "list_of_dictionaries, expected",
    [
        ([], "Операции отсутствуют"),
        ([1, 2, 3], "Некорректные данные"),
        ("", "Некорректные данные"),
        ({}, "Некорректные данные"),
    ],
)
def test_sort_by_date_wrong(list_of_dictionaries: Any, expected: str) -> None:
    assert sort_by_date(list_of_dictionaries) == expected


@pytest.mark.parametrize('search_word, expected', [('я', []), ('перевод организации', [
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
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ])])
def test_process_bank_search(transactions, search_word, expected):
    assert process_bank_search(transactions, search_word) == expected


@pytest.mark.parametrize('categories, expected', [([], {}), (['Перевод организации'], {'Перевод организации':2})])
def test_process_bank_operations(transactions, categories, expected):
    assert process_bank_operations(transactions, categories) == expected