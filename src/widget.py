import masks


def mask_account_card(card: str) -> str:
    """Принимает на вход строку, содержащую тип и номер карты или счета, возвращает строку с маской"""
    result = ''
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
