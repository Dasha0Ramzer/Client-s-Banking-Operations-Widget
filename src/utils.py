import json
import os
from typing import Any


def financial_transaction_data(path_to_the_JSON_file: str) -> Any:
    """Функция, считывающая JSON-файл и выводящая содержимое"""
    if not os.path.exists(path_to_the_JSON_file):
        return []
    try:
        with open(path_to_the_JSON_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return []
