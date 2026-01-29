from typing import Any, Callable, List
from unittest.mock import mock_open, patch

from src.utils import financial_transaction_data


@patch(
    "builtins.open", new_callable=mock_open, read_data='[{"amount": "31957.58", "description": "Перевод организации"}]'
)
@patch("os.path.exists", return_value=True)
def test_financial_transaction_data(mock_exists: Any, mock_file: Callable[..., Any]) -> None:
    result: List[dict] = financial_transaction_data("path_to_the_JSON_file")
    expected: List[dict] = [{"amount": "31957.58", "description": "Перевод организации"}]
    assert result == expected


@patch("os.path.exists", return_value=False)
def test_financial_transaction_data_2(mock_exists: Any) -> None:
    result: List[dict] = financial_transaction_data("path_to_the_JSON_file")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="amount = 31957.58")
@patch("os.path.exists", return_value=True)
def test_financial_transaction_data_3(mock_exists: Any, mock_file: Callable[..., Any]) -> None:
    result: List[dict] = financial_transaction_data("path_to_the_JSON_file")
    assert result == []
