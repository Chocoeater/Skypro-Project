def filter_by_state(list_of_data: list, state='EXECUTED') -> list:
    """Принимает список словарей и опционально значение для ключа state,
    возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""
    result_list = []
    for data in list_of_data:
        if data['state'] == state:
            result_list.append(data)
    return result_list
