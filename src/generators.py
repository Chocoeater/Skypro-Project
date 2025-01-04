from typing import Dict, Generator, List, Any


def filter_by_currency(transactions: List[Any], currency: str) -> Generator[Dict]:
    """Генератор, который принимает список словарей и возвращает только операции с валютой currency"""
    filtered_transactions = [d for d in transactions if d]
    if filtered_transactions:
        for transaction in filtered_transactions:
            if transaction.get('operationAmount'):
                if transaction.get('operationAmount').get('currency'):
                    if transaction.get('operationAmount').get('currency').get('code') == currency:
                        yield transaction
    else:
        raise ValueError('Список транзакций пуст!')


def transaction_descriptions(transactions: List[Dict]) -> Generator[str]:
    """Генератор, который принимает список словарей и возвращает описание операции"""
    filtered_transactions = [d for d in transactions if d]
    if filtered_transactions:
        for transaction in filtered_transactions:
            yield str(transaction.get('description'))
    else:
        raise ValueError('Список транзакций пуст!')


def card_number_generator(start: int, end: int) -> Generator[str]:
    """Генератор, который принимает диапазон значений и возвращает номера карты из этого диапазона"""
    if start > 0 and end <= 9999999999999999:
        for num in range(start, end + 1):
            fill = str(num).zfill(16)
            result = [fill[i:i + 4] for i in range(0, len(fill), 4)]
            yield ' '.join(result)
    else:
        raise AttributeError('Параметры генерации вне допустимого диапазона')
