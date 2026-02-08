from typing import Any, Callable, List
from unittest.mock import mock_open, patch

import pandas as pd

from src.file_readers import csv_file_reader, xlsx_file_reader


@patch("builtins.open", new_callable=mock_open, read_data="id;state\n650703;EXECUTED")
def test_csv_file_reader(mock_file: Callable[..., Any]) -> None:
    result: List[dict] = csv_file_reader("path_to_the_CSV_file")
    expected: List[dict] = [
        {
            "id": 650703,
            "state": "EXECUTED",
        }
    ]
    assert result == expected


excel_content = pd.DataFrame({"ID": [650703], "State": ["EXECUTED"]})


@patch("pandas.read_excel")
def test_xlsx_file_reader(mock_read_excel: Any) -> None:
    mock_read_excel.return_value = excel_content
    result: List[dict] = xlsx_file_reader("path_to_the_XLSX_file")
    expected: List[dict] = [
        {
            "ID": 650703,
            "State": "EXECUTED",
        }
    ]
    assert result == expected
