from re import match

def name_validator(name):
    return bool(match("^(([A-Z]{1}([a-z]*)((\')?[a-z]*)(\,)?(\s)?)*)$", name))


def brand_validator(data, separator=" "):
    pattern = "^(([A-Z]+([a-z]*)((\')?[a-z]*)(\s)?(\&)?(\s)?)*)$"
    if isinstance(data, str):
        data = data.split(separator)
    if isinstance(data, list):
        for element in data:
            if not match(pattern, element):
                return False
        return True
    else:
        return False

def sizes_validator(sizes):
    return bool(match("^([0-9]+((\.)?[0-9]*)(\,)?(\s)?)+$", sizes))


def merchants_validator(merchants):
    return bool(match("^(([A-Z]+([a-z]*)((\')?([a-z]*)(\.)?[a-z]*)(\s)?)*)$", merchants))

