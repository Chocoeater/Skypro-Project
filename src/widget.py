from . import masks


def mask_account_card(card: str) -> str:
    """Принимает на вход строку, содержащую тип и номер карты или счета, возвращает строку с маской"""
    type_card = []
    account = ''
    list_of_card = card.split()
    for element in list_of_card:
        if element.isdigit():
            account = element
        else:
            type_card.append(element)
    if len(account) == 16:
        result = ' '.join(type_card) + ' ' + masks.get_mask_card_number(account)
        return result
    elif len(account) == 20:
        result = ' '.join(type_card) + ' ' + masks.get_mask_account(account)
        return result


def get_date(date_and_time: str) -> str:
    """Пнимает строку формата 2024-03-11T02:26:18.671407, возвращает строку формата ДД.ММ.ГГГГ"""
    date = date_and_time[:10].split('-')
    date.reverse()
    return '.'.join(date)
