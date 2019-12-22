import re


def price_validator(price):
    if re.match('^\d+\.{0,1}\d*$', str(price)):
        return True
    return False

def code_validator(country_code):
    if re.match('^[A-Z]{2}$', str(country_code)):
        return True
    return False

def city_validator(city):
    if re.match('^([A-Z](?:[a-z]+[- ]*))+$', str(city)):
        return True
    return False

def street_validator(street):
    if re.match('^(?:[\w./,:; ])+$', str(street)):
        return True
    return False