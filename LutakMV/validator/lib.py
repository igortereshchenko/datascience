import re


def st_assem_validator(text):
    text = str(text)
    return bool(re.match(r'^\d+$', text))


def spc_latin_validator(text):
    return bool(re.match(r'^([A-Z]+\s?)*$', text))


def inf_canopy_validator(text):
    return bool(re.match(r'^[Y,y]es$|^[N,n]o$', text))

def zipcode_validator(text):
    text = str(text)
    return bool(re.match(r'^\d{5}$|^0$', text))