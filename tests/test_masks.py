import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_base_case(card_number):
    assert get_mask_card_number('1234123412341234') == card_number


def test_get_mask_account_base_case(account_number):
    assert get_mask_account('12341234123412341234') == account_number


@pytest.mark.parametrize('value, expected', [
    (1234123412341234, '1234 12** **** 1234'),
    (1234, '0'),
    (123412341234123412, '1234 12** **** 1234 12'),
    ('', '0'),
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('value, expected', [
    (12341234123412341234, '**1234'),
    (1234, '0'),
    (123412341234123412, '0'),
    ('', '0'),
    (1234123412341234123412, '0')
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
