import re

def name_validator():
    name = input("Введіть назву:")
    if bool(re.match("^(([A-Z]{1}([a-z]*)((\')?[a-z]*)(\,)?(\s)?)*)$", name)):
        pass
    else:
        print("Назва введена неправильно!")
        return name_validator()
    name.split()
    return name

def brand_validator():
    brand = input("Введіть бренд:")
    if bool(re.match("^(([A-Z]+([a-z]*)((\')?[a-z]*)(\s)?(\&)?(\s)?)*)$", brand)):
        pass
    else:
        print("Бренд введена неправильно!")
        return brand_validator()
    brand.split()
    return brand

def sizes_validator():
    sizes = input("Введіть розміри взуття:")
    if bool(re.match("^([0-9]+((\.)?[0-9]*)(\,)?(\s)?)+$", sizes)):
        pass
    else:
        print("Розміри введено неправильно!")
        return sizes_validator()
    sizes.split()
    return sizes

def merchants_validator():
    merchants = input("Покупець:")
    if bool(re.match("^(([A-Z]+([a-z]*)((\')?([a-z]*)(\.)?[a-z]*)(\s)?)*)$", merchants)):
        pass
    else:
        print("Інформація  введена неправильно!")
        return merchants_validator()
    merchants.split()
    return merchants

