def filter_by_state(input_dict_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает на вход список словарей по банковским операциям и возвращает
    новый список, с выборкой тех, у которых ключ 'state' содержит переданное в функцию значение
    """

    if len(input_dict_list) == 0:
        return []
    new_list_with_state = []
    for operation in input_dict_list:
        if operation["state"] == state:
            new_list_with_state.append(operation)
    return new_list_with_state


def sort_by_date(dict_list_input: list, descending_order: bool = True) -> list:
    """Функция принимает на вход список словарей по банковским операциям и возвращает
    новый список, отсортированный в заданном вторым параметром порядке
    """
    return sorted(dict_list_input, key=lambda x: x["date"], reverse=descending_order)
