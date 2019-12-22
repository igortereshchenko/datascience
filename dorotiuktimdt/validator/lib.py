import re


def ean_validator():
    ean = input('Введіть значення унікального штрих-коду: ')
    if bool(re.match('^[0-9]{1}\.[0-9]{5}E\+[0-9]{2}$', ean)):
        pass
    else:
        print('Error')
        return ean_validator()
    return ean



def keys_validator():
    key_text_1 = input('Введіть ключовий вираз №1: ')
    if bool(re.match('^([a-z]+)$', key_text_1)):
        pass
    else:
        print('Error')
        return keys_validator()
    key_text_2 = input('Введіть ключовий вираз №2: ')
    if bool(re.match('^([a-z]+)$', key_text_2)):
        pass
    else:
        print('Error')
        return keys_validator()
    key_num_1 = input('Введіть код для ключового виразу №1: ')
    if bool(re.match('^([0-9]{12})$', key_num_1)):
        pass
    else:
        print('Error')
        return keys_validator()
    key_num_2 = input('Введіть код для ключового виразу №2: ')
    if bool(re.match('^([0-9]{12})$', key_num_2)):
        pass
    else:
        print('Error')
        return keys_validator()

    keys = {key_text_1: key_num_1, key_text_2: key_num_2}
    return keys



def manufacturer_validator():
    manufacturer = input('Введіть назву виробника: ')
    if bool(re.match('^(([A-Z]+([a-z]*)((\')?([a-z]*)(\.)?[a-z]*)(\s)?)*)$', manufacturer)):
        pass
    else:
        print('Error')
        return manufacturer_validator()
    return manufacturer


def brand_validator():
    brand = input('Введіть назву бренда: ')
    if bool(re.match('^(([A-Z]+([a-z]*)((\')?([a-z]*)(\.)?[a-z]*)(\s)?)*)$', brand)):
        pass
    else:
        print('Error')
        return brand_validator()
    return brand


