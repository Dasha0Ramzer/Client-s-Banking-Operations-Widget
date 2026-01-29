import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")
headers = {"apikey": f"{api_key}"}
url = "https://api.apilayer.com/exchangerates_data/convert"


def currency_converter(transaction: dict) -> float:
    """Функция конвертации иностранной валюты в рубли"""
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        payload = {"amount": transaction["operationAmount"]["amount"], "from": currency, "to": "RUB"}
        response = requests.get(url, headers=headers, params=payload)
        status_code = response.status_code
        if status_code == 200:
            result = response.json()
            return result["result"]
        else:
            return f"Запрос не был успешным. Возможная причина: {response.reason}"
