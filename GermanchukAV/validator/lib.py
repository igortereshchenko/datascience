import re

def host_id_validator(data):
    match = re.match('^\d{4,8}$', data)
    if match:
        return int(match.group())
    else:
        print('This data is not valid')


def country_code_validator(data):
    match = re.match('^[A-Z]+$', data)
    if match:
        return match.group()
    else:
        print('This data is not valid')


def bed_type_validator(data):
    match = re.match('^[A-Z]([a-z-])+(\s[A-Z][a-z]+)*$', data)
    if match:
        return match.group()
    else:
        print('This data is not valid')

def price_validator(data):
    match = re.match('^\d+.\d+$', data)
    if match:
        return float(match.group())
    else:
        print('This data is not valid')

