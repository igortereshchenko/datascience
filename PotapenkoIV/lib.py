from re import match


def cen_year(data):
    pattern = "^[0-9]{4}$"
    return match(pattern, data)


def tree_loc(data):
    pattern = "([A-Z]+\s?)*"
    return match(pattern, data)


def spc_latin(data):
    pattern = "([A-Z]+\s?)*"
    return match(pattern, data)


def horz_other(data):
    pattern = "([A-Z]+\s?)*"