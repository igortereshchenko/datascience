from re import match


def brand_validator(name_of_brand):
    """
    if validation is correct return True
    :param name_of_brand: str , brand
    :return:bool
    """
    if match('^([a-zA-z]\s{0,1})*', str(name_of_brand)):
        return True
    return False


def pricecount_validator(price):
    """
    if validation is correct return Ture
    :param price: float, value of price
    :return: bool
    """
    if match("^\d+\.{0,1}\d*$", str(price)):
        return True
    return False


def quantities_validator(quantities):
    """
    if validation is correct return True
    :param quantities: dict, must has 3 key
    :return: bool
    """
    key_list = ["dateSeen", "sourceURLs", "value"]
    if isinstance(quantities, str):
        if match(
                '^\{\"(dateSeen)\"\:\s*\[(\"[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])T([0-1]\d|2[0-3])(:[0-5]\d){2}\.\d{3}Z\")(\,\s*\"[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])T([0-1]\d|2[0-3])(:[0-5]\d){2}\.\d{3}Z\")*\]\,\s*\"(sourceURLs)\"\:\s*\"[a-zA-Z:/.-1234567890]*\"\,\s*\"value\"\:\s*\d*\}$',
                quantities):
            quantities = dict(quantities)

    if isinstance(quantities, dict):
        count = 0
        for key in key_list:
            if key in key_list:
                count += 1
        if count == 3:
            for key in key_list:
                if isinstance(quantities[key], list):
                    if len(quantities[key]):
                        count -= 1
                elif match('https:\/\/[a-zA-Z]*.[a-zA-Z]*', str(quantities[key])):
                    count -= 1
                elif match('\d+$', str(quantities[key])):
                    count -= 1
            if count == 0:
                return True
    else:
        return False


def skus_validator(skus):
    """
    if validation is correct return True
    :param skus: dict, must has 2 keys
    :return: bool
    """
    key_list = ["sourceURLs", "value"]
    if isinstance(skus, str):
        if match(
                '^\{\"(sourceURLs)\"\:\s*\"[a-zA-Z:/.-1234567890]*\"\,\s*\"value\"\:\s*\"\d*\"\}$',
                skus):
            skus = dict(skus)

    if isinstance(skus, dict):
        count = 0
        for key in key_list:
            if key in key_list:
                count += 1
        if count == 2:
            for key in key_list:
                if match('https:\/\/[a-zA-Z]*.[a-zA-Z]*', skus[key]):
                    count -= 1
                if match('\d+$', skus[key]):
                    count -= 1
            if count == 0:
                return True
    else:
        return False
