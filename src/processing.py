from src.widget import get_date


def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    '''Функция, возвращающая список словарей по указанному значению ключа "state"'''
    new_list = []
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == state:
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_of_dictionaries: list[dict], reversed: bool = True) -> list[dict]:
    """Функция, сортирующая список словарей по убыванию даты"""
    new_list = sorted(list_of_dictionaries, key = lambda dictionary: dictionary['date'], reverse = reversed)
    return new_list
