from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict]:
    """Генератор, который принимает список словарей и возвращает только операции с валютой currency"""
    for transaction in transactions:
        if transaction.get('operationAmount').get('currency').get('code') == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str]:
    """Генератор, который принимает список словарей и возвращает описание операции"""
    for transaction in transactions:
        yield str(transaction.get('description'))


def card_number_generator(start: int, end: int) -> Generator[str]:
    """Генератор, который принимает диапазон значений и возвращает номера карты из этого значения"""
    for num in range(start, end + 1):
        fill = str(num).zfill(16)
        result = [fill[i:i + 4] for i in range(0, len(fill), 4)]
        yield ' '.join(result)
