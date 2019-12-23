import re


def id_validator():
    id = input('Введіть індивідуальну назву: ')
    if bool(re.match('^n{2}_{1}m{3}[0-9]{3}$', id)):
        pass
    else:
        print('Не правильно введенна назва!Введіть знову:')
        return id_validator()
    return
def name_validator():
    name = input('Введіть назву взуття:')
    if bool(re.match('^([A-Z]*[a-z]*)+$', name)):
        pass
    else:
        print('Не правильно введенна назва!Введіть знову:')
        return name_validator()
    return name
def reviews_validator():
    reviews = input('Введіть відгук:')
    if bool(re.match('^([A-Z]*[a-z]*)+$', reviews)):
        pass
    else:
        print('Не правильно введенний відгук!Введіть знову:')
        return reviews_validator()
    return reviews
def upc_validator():
    upc = input('Введіть індивідуальний код:')
    if bool(re.match('^[0-9]{6}$', upc)):
        pass
    else:
        print('Не правильно введенний код!Введіть знову:')
        return upc_validator()
    return upc

