import re


def spc_latin_validator(text):
    return bool(re.match(r'^([A-Z]+\s?)*$', text))


def cen_year_validator(text):
    text = str(text)
    return bool(re.match(r'^\d+$', text))


def wire_other_validator(text):
    return bool(re.match(r'^[Y,y]es$|^[N,n]o$', text))


def inf_other_validator(text):
    return bool(re.match(r'^[Y,y]es$|^[N,n]o$', text))