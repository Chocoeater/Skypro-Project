from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Принимает номер карты в виде числа, возвращает маску формата 1234 12** **** 1234 в виде строки"""
    if len(str(card_number)) >= 16:
        card_number = str(card_number)
        mask_card = card_number[0:6] + "*" * 6 + card_number[12:]
        result = " ".join([mask_card[i: i + 4] for i in range(0, len(mask_card), 4)])
        return result
    else:
        return '0'


def get_mask_account(number_account: Union[int, str]) -> str:
    """Принимает номер счета в виде числа, возвращает маску формата **1234 в виде строки"""
    if len(str(number_account)) == 20:
        number_account = str(number_account)
        return "**" + number_account[-4:]
    else:
        return '0'
