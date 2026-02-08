from typing import Any, Union

from src.file_readers import csv_file_reader, xlsx_file_reader
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date
from src.utils import financial_transaction_data
from src.widget import get_date, mask_account_card


def main() -> Any:
    my_data: Any = filter_by_state(data, status)

    if sort_date:
        my_data = sort_by_date(my_data, sorted_dates)

    if search_word:
        my_data = process_bank_search(my_data, search_word)

    if rub_transaction:
        my_data = list(filter_by_currency(my_data, "RUB"))

    list_operations = list(transaction_descriptions(my_data))
    dict_operations = process_bank_operations(my_data, list(set(list_operations)))
    count_operations = sum(dict_operations.values())
    if count_operations == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {count_operations}")
    print()

    for dict_ in my_data:
        print(f"{get_date(dict_['date'])} {list(transaction_descriptions([dict_]))[0]}")
        if dict_.get("from") and isinstance(dict_.get("from"), str):
            print(f"{mask_account_card(dict_['from'])} -> {mask_account_card(dict_['to'])}")
        else:
            print(f"{mask_account_card(dict_['to'])}")
        if "operationAmount" in dict_:
            print(f'Сумма: {dict_["operationAmount"]["amount"]} {dict_['operationAmount']["currency"]["name"]}')
        else:
            print(f'Сумма: {dict_["amount"]} {dict_['currency_name']}')
        print()


print(
    """Привет!
Добро пожаловать в программу работы с банковскими транзакциями."""
)
print(
    """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
)
while True:
    data = input("Введите число: ")
    if data == "1":
        print("Для обработки выбран JSON-файл.")
        data = financial_transaction_data("./data/operations.json")
        break
    elif data == "2":
        print("Для обработки выбран CSV-файл.")
        data = csv_file_reader("./data/transactions.csv")
        break
    elif data == "3":
        print("Для обработки выбран XLSX-файл.")
        data = xlsx_file_reader("./data/transactions_excel.xlsx")
        break
    elif not data.isdigit():
        print("Вы ввели не число.")
    else:
        print("Такой пункт меню отсутствует. Повторите попытку.")

print()
print(
    """Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING."""
)
while True:
    status = input("Статус: ").upper()
    if status == "EXECUTED":
        print('Операции отфильтрованы по статусу "EXECUTED".')
        break
    elif status == "CANCELED":
        print('Операции отфильтрованы по статусу "CANCELED".')
        break
    elif status == "PENDING":
        print('Операции отфильтрованы по статусу "PENDING".')
        break
    else:
        print(f'Статус операции "{status}" недоступен. Повторите попытку.')

print()
print("Отсортировать операции по дате? Да/Нет")
while True:
    sort_date: Union[str, bool] = input("Введите ответ: ").lower()
    if sort_date == "да":
        sort_date = True
        print()
        print("Отсортировать по возрастанию или по убыванию?")
        while True:
            sorted_dates_str = input("Введите ответ: ").lower()
            if sorted_dates_str == "по убыванию":
                sorted_dates = True
                break
            elif sorted_dates_str == "по возрастанию":
                sorted_dates = False
                break
            else:
                print('Неверный ввод. Введите "по убыванию" или "по возрастанию"')
        break
    elif sort_date == "нет":
        sort_date = False
        break
    else:
        print("Повторите попытку.")

print()
print("Выводить только рублевые транзакции? Да/Нет")
while True:
    rub_transaction: Union[str, bool] = input("Введите ответ: ").lower()
    if rub_transaction == "да":
        rub_transaction = True
        break
    elif rub_transaction == "нет":
        rub_transaction = False
        break
    else:
        print("Повторите попытку.")

print()
print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
while True:
    search_word_str = input("Введите ответ: ").lower()
    if search_word_str == "да":
        search_word = input("Введите слово для поиска: ")
        break
    elif search_word_str == "нет":
        search_word = ""
        break
    else:
        print("Повторите попытку.")

print()
print("Распечатываю итоговый список транзакций...")
print()

main()
