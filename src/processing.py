from typing import Union


def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> Union[list[dict], str]:
    '''Функция, возвращающая список словарей по указанному значению ключа "state"'''
    if not isinstance(list_of_dictionaries, list):
        return "Некорректные данные"
    if len(list_of_dictionaries) == 0:
        return "Операции отсутствуют"
    new_list = []
    for dictionary in list_of_dictionaries:
        if not isinstance(dictionary, dict):
            return "Некорректные данные"
        if dictionary["state"] == state:
            new_list.append(dictionary)
    if len(new_list) == 0:
        return "Данный статус отсутствует"
    return new_list


def sort_by_date(list_of_dictionaries: list[dict], reversed: bool = True) -> Union[list[dict], str]:
    """Функция, сортирующая список словарей по убыванию даты"""
    if not isinstance(list_of_dictionaries, list):
        return "Некорректные данные"
    if len(list_of_dictionaries) == 0:
        return "Операции отсутствуют"
    for dictionary in list_of_dictionaries:
        if not isinstance(dictionary, dict):
            return "Некорректные данные"
    new_list = sorted(list_of_dictionaries, key=lambda dictionary: dictionary["date"], reverse=reversed)
    return new_list
