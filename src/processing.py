from typing import List, Dict


def filter_by_state(list_of_data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Принимает список словарей и опционально значение для ключа state,
    возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""
    result_list = []
    for data in list_of_data:
        if data.get('state') == state:
            result_list.append(data)
    return result_list


def sort_by_date(list_of_data: List[Dict], decreasing: bool = True) -> List[Dict]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате."""
    return sorted(list_of_data, key=lambda date: date['date'], reverse=decreasing)

