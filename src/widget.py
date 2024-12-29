from . import masks


def mask_account_card(card: str) -> str:
    """Принимает на вход строку, содержащую тип и номер карты или счета, возвращает строку с маской"""
    if type(card) is not str:
        raise TypeError('Ожидается строковый формат')
    type_card = []
    account = ''
    list_of_card = card.split()
    for element in list_of_card:
        if element.isdigit():
            account = element
        else:
            type_card.append(element)
    if 20 > len(account) >= 16:
        result = ' '.join(type_card) + ' ' + masks.get_mask_card_number(account)
        return result
    elif len(account) == 20:
        result = ' '.join(type_card) + ' ' + masks.get_mask_account(account)
        return result
    else:
        raise ValueError('Неверный формат номера счета или карты')


def get_date(date_and_time: str) -> str:
    """Принимает строку формата 2024-03-11T02:26:18.671407, возвращает строку формата ДД.ММ.ГГГГ"""
    if type(date_and_time) is not str:
        raise TypeError('Ожидается строковый формат')
    date = date_and_time[:10].split('-')
    for d in date:
        if not d.isdigit():
            raise ValueError('Неверный формат даты, ожидается формат ГГГГ-ММ-ДД...')
    for i, d in (4, 2, 2), date:
        if len(d) != i:
            raise ValueError('Неверный формат даты, ожидается формат ГГГГ-ММ-ДД...')
    date.reverse()
    return '.'.join(date)
