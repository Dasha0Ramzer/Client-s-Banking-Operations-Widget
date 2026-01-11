def filter_by_state(list_of_dictionaries: list, state='EXECUTED') -> list:
    new_list = []
    for dictionary in list_of_dictionaries:
        if dictionary['state'] == state:
            new_list.append(dictionary)
    return new_list
