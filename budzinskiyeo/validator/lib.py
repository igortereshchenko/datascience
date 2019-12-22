from re import match


def flavors_validator(data):
    pattern = "^[A-z0-9]{8}(-[A-z0-9]{4}){3}-[A-z0-9]{12}$"
    return match(pattern, data)


def count_validator(data):
    pattern = "^[0-9]{1,}$"
    return match(pattern, data)


def categories_validator(data, separator=" "):
    pattern = "^[A-z0-9\\'\\-\\s]+$"
    if isinstance(data, str):
        data = data.split(separator)
    if isinstance(data, list):
        for element in data:
            if not match(pattern, element):
                return False
        return True
    else:
        return False


def brand_validator(data, separator=" "):
    pattern = "^[A-z0-9\\'\\-\\s]+$"
    if isinstance(data, str):
        data = data.split(separator)
    if isinstance(data, list):
        for element in data:
            if not match(pattern, element):
                return False
        return True
    else:
        return False
