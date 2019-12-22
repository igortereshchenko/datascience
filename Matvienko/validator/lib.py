import re


def cen_year_validator(message):
    n = str(message)
    return bool(re.match(r"^\d{4}$", n))


def horz_plant_validator(message):
    n = str(message)
    return bool(re.match(r"(^Yes$|^No$|^yes$|^no$)", n))


def vert_wall_validator(message):
    n = str(message)
    return bool(re.match(r"(^Yes$|^No$|^yes$|^no$)", n))


def sidw_raise_validator(message):
    n = str(message)
    return bool(re.match(r"(^Yes$|^No$|^yes$|^no$)", n))


