import re

def zip_city_validator(text):
    return bool(re.match(r'^([A-Z]\w+\s?)*$', text))


def borocode_validator(text):
    text = str(text)
    return bool(re.match(r'^[1-5]$', text))


def boroname_validator(text):
    return bool(re.match(r'^([A-Z]\w+\s?)*$', text))


def cb_num_validator(text):
    text = str(text)
    return bool(re.match(r'^\d{1}$', text))