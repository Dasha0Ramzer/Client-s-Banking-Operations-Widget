from typing import Any

import pandas as pd


def csv_file_reader(path_to_the_CSV_file: str) -> Any:
    """Функция, считывающая CSV-файл и выводящая содержимое"""

    transactions = pd.read_csv(path_to_the_CSV_file, sep=";")
    data = transactions.to_dict(orient="records")
    return data


# print(csv_file_reader('../data/transactions.csv'))


def xlsx_file_reader(path_to_the_XLSX_file: str) -> Any:
    """Функция, считывающая XLSX-файл и выводящая содержимое"""

    transactions = pd.read_excel(path_to_the_XLSX_file)
    data = transactions.to_dict(orient="records")
    return data


# print(xlsx_file_reader('../data/transactions_excel.xlsx'))
