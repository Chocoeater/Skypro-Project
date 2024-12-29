import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card_card(mask_card):
    assert mask_account_card('Visa Platinum 8990922113665229') == mask_card


def test_mask_account_card_acc(mask_acc):
    assert mask_account_card('Счет 73654108430135874305') == mask_acc


@pytest.mark.parametrize('value, expected', [
    (
            'Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'
    ),
    (
            'MasterCard 715830073472675822', 'MasterCard 7158 30** **** 6758 22'
    ),
    (
            'Счет 35383033474447895560', 'Счет **5560'
    )
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_mask_account_card_type():
    with pytest.raises(TypeError, match='Ожидается строковый формат'):
        mask_account_card(123)


def test_mask_account_card_value():
    with pytest.raises(ValueError, match='Неверный формат номера счета или карты'):
        mask_account_card('Maestro 159683786870519')


def test_mask_account_card_value_1():
    with pytest.raises(ValueError, match='Неверный формат номера счета или карты'):
        mask_account_card('Карась228')


def test_get_date_base_case(date):
    assert get_date('2024-12-29') == date


def test_get_date_value():
    with pytest.raises(ValueError, match='Неверный формат даты, ожидается формат ГГГГ-ММ-ДД...'):
        get_date('24-12-2024')


def test_get_date_value_letters():
    with pytest.raises(ValueError, match='Неверный формат даты, ожидается формат ГГГГ-ММ-ДД...'):
        get_date('Двадцать четвертое декабря две тысячи двадцать четвертого года')


def test_get_date_value_empty():
    with pytest.raises(ValueError, match='Неверный формат даты, ожидается формат ГГГГ-ММ-ДД...'):
        get_date('')


def test_get_date_value_digits():
    with pytest.raises(TypeError, match='Ожидается строковый формат'):
        get_date(24.12)
