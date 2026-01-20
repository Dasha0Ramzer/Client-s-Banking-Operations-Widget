from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_information, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Некорректный номер карты/счета"),
        ([], "Некорректный номер карты/счета"),
        ({}, "Некорректный номер карты/счета"),
        ([1, 2], "Некорректный номер карты/счета"),
        (["Visa Platinum", 2], "Некорректный номер карты/счета"),
        ("Visa Platinum aaaabbbbccccdddd", "Некорректный номер карты/счета"),
    ],
)
def test_mask_account_card(account_information: Any, expected: Any) -> None:
    assert mask_account_card(account_information) == expected
    with pytest.raises(TypeError):
        mask_account_card(0)
    with pytest.raises(TypeError):
        mask_account_card(123)
    with pytest.raises(TypeError):
        mask_account_card(1234567890123456)


@pytest.mark.parametrize(
    "date_another_format, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("3219-67-93T18:35:29.512364", "Такой даты не существует"),
        ("219-67-93T18:35:29.512364", "Некорректные данные"),
        ("", "Некорректные данные"),
        ([], "Некорректные данные"),
        ({}, "Некорректные данные"),
        ([1, 2], "Некорректные данные"),
        ("aaaaaaaabbbbbbccccccdddddd", "Некорректные данные"),
    ],
)
def test_get_date(date_another_format: Any, expected: Any) -> None:
    assert get_date(date_another_format) == expected
    with pytest.raises(TypeError):
        get_date(0)
    with pytest.raises(TypeError):
        get_date(123)
    with pytest.raises(TypeError):
        get_date(12345678901234567890)
