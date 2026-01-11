from src.widget import get_date


def filter_by_state(list_of_dictionaries: list[dict], state: str='EXECUTED') -> list[dict]:
    '''Функция, возвращающая список словарей по указанному значению ключа "state"'''
    new_list = []
    for dictionary in list_of_dictionaries:
        if dictionary['state'] == state:
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_of_dictionaries: list[dict], reversed: bool=True) -> list[dict]:
    '''Функция, сортирующая список словарей по убыванию даты'''
    list_date = []
    #Создаем новый список, содержащий только даты, созданный с помощью функции get_date
    for dictionary in list_of_dictionaries:
        list_date.append(get_date(dictionary['date']).split('.'))
    #Изменяем даты в формате ГГГГ ММ ДД
    for i in list_date:
        i.reverse()
    #Сортируем даты в порядке убывания
    list_date.sort(reverse=True)
    #Создаем новый список с корректным форматом даты (ДД.ММ.ГГГГ)
    new_list_date = []
    for date in list_date:
        date.reverse()
        new_list_date.append('.'.join(date))
    #Сортируем список словарей по дате
    new_list_dict =[]
    for date in new_list_date:
        for dict_ in list_of_dictionaries:
            if date == get_date(dict_['date']):#Используем функцию get_date
                new_list_dict.append(dict_)
                break
    return new_list_dict






    new_list = sorted(list_of_dictionaries, key=lambda dictionary: get_date(dictionary['date']).split('.'), reverse=reversed)
    return new_list
