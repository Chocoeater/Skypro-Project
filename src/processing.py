def filter_by_state(list_of_data: list, state: str = 'EXECUTED') -> list:
    """Принимает список словарей и опционально значение для ключа state,
    возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""
    result_list = []
    for data in list_of_data:
        if data['state'] == state:
            result_list.append(data)
    return result_list


def sort_by_date(list_of_data: list, reverse: bool = False) -> list:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате.
    Использует пузырьковый алгоритм сортировки"""
    result = list_of_data
    if reverse:
        for i in range(len(result) - 1):
            for j in range(len(result) - i):
                if result[j]['date'][:10] > result[j + 1]['date'][:10]:
                    result[j]['date'][:10], result[j + 1]['date'][:10] = \
                        result[j + 1]['date'][:10], result[j]['date'][:10]
    else:
        for i in range(len(result) - 1):
            for j in range(len(result) - 1 - i):
                if result[j]['date'][:10] < result[j + 1]['date'][:10]:
                    result[j]['date'], result[j + 1]['date'] = \
                        result[j + 1]['date'], result[j]['date']
    return result
