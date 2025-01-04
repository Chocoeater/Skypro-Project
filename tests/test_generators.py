import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

test_data = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
]


def test_filter_by_currency_base_case(filtered_by_currency):
    generator = filter_by_currency(test_data, 'USD')
    assert next(generator) == filtered_by_currency


@pytest.mark.parametrize('value, expected', [
    ('USD',
     [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
       'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
       'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
      {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
       'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
       'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
       'to': 'Счет 75651667383060284188'}, {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
                                            'operationAmount': {'amount': '56883.54',
                                                                'currency': {'name': 'USD', 'code': 'USD'}},
                                            'description': 'Перевод с карты на карту',
                                            'from': 'Visa Classic 6831982476737658',
                                            'to': 'Visa Platinum 8990922113665229'}]),
    ('RUB',
     [{'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
       'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
       'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
       'to': 'Счет 74489636417521191160'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
                                            'operationAmount': {'amount': '67314.70',
                                                                'currency': {'name': 'руб.', 'code': 'RUB'}},
                                            'description': 'Перевод организации',
                                            'from': 'Visa Platinum 1246377376343588',
                                            'to': 'Счет 14211924144426031657'}])
])
def test_filter_by_currency(value, expected):
    generator = filter_by_currency(test_data, value)
    assert list(generator) == expected


def test_transaction_descriptions():
    generator = transaction_descriptions(test_data)
    assert list(generator) == ['Перевод организации', 'Перевод со счета на счет', 'Перевод со счета на счет',
                               'Перевод с карты на карту', 'Перевод организации']


@pytest.mark.parametrize('value_1, value_2, expected', [
    (1, 4, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003', '0000 0000 0000 0004']),
    (9999999999999995, 9999999999999999,
     ['9999 9999 9999 9995', '9999 9999 9999 9996', '9999 9999 9999 9997', '9999 9999 9999 9998',
      '9999 9999 9999 9999'])
])
def test_card_number_generator(value_1, value_2, expected):
    generator = card_number_generator(value_1, value_2)
    assert list(generator) == expected


def test_filter_by_currency_empty():
    with pytest.raises(ValueError, match='Список транзакций пуст!'):
        generator = filter_by_currency([{}], 'RUB')
        next(generator)


def test_transaction_descriptions_empty():
    with pytest.raises(ValueError, match='Список транзакций пуст!'):
        generator = transaction_descriptions([{}])
        next(generator)


def test_card_number_generator_out_of_range():
    with pytest.raises(AttributeError, match='Параметры генерации вне допустимого диапазона'):
        generator = card_number_generator(0, 100000000000000000)
        next(generator)
