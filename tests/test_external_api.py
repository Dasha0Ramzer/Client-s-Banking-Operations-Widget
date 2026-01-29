import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import currency_converter

load_dotenv(".env")
api_key = os.getenv("API_KEY")


def test_currency_converter() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 618658.363805}
        transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": 8221.37}}
        assert currency_converter(transaction) == "Сумма = 618658.36 руб."
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert",
            headers={"apikey": f"{api_key}"},
            params={"amount": 8221.37, "from": "USD", "to": "RUB"},
        )


def test_currency_converter_2() -> None:
    transaction = {"operationAmount": {"currency": {"code": "RUB"}, "amount": 100}}
    assert currency_converter(transaction) == "Сумма = 100 руб."


def test_currency_converter_3() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.reason = "Not Found"

        transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": 1}}
        assert currency_converter(transaction) == "Запрос не был успешным. Возможная причина: Not Found"
