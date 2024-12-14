def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты в виде числа, возвращает маску формата 1234 12** **** 1234 в виде строки"""
    card_number = str(card_number)
    mask_card = card_number[0:6] + "*" * 6 + card_number[12:]
    result = " ".join([mask_card[i: i + 4] for i in range(0, len(mask_card), 4)])
    return result


def get_mask_account(number_account: int) -> str:
    """Принимает номер счета в виде числа, возвращает маску формата **1234 в виде строки"""
    number_account = str(number_account)
    return "**" + number_account[-4:]
go