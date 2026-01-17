from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("0000000000000000", "0000 00** **** 0000"),
        ("", "Некорректный номер карты"),
        ([], "Некорректный номер карты"),
        ({}, "Некорректный номер карты"),
        ([1, 2], "Некорректный номер карты"),
        ("aaaabbbbccccdddd", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number: Any, expected: Any) -> None:
    assert get_mask_card_number(card_number) == expected
    with pytest.raises(TypeError):
        get_mask_card_number(0)
        get_mask_card_number(123)
        get_mask_card_number(1234567890123456)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("00000000000000000000", "**0000"),
        ("", "Некорректный номер счета"),
        ([], "Некорректный номер счета"),
        ({}, "Некорректный номер счета"),
        ([1, 2], "Некорректный номер счета"),
        ("aaaaabbbbbcccccddddd", "Некорректный номер счета"),
    ],
)
def test_get_mask_account(account_number: Any, expected: str) -> None:
    assert get_mask_account(account_number) == expected
    with pytest.raises(TypeError):
        get_mask_account(0)
        get_mask_account(123)
        get_mask_account(12345678901234567890)
