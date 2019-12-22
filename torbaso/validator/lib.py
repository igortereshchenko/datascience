import re


def country_validator(country):
    textlookfor = r"[A-Z][a-z]{5}\s[A-Z][a-z]{5}"
    while not re.match(textlookfor,country):
        country = input('Enter valid country')
    return country



def name_validator(name):
    textlookfor = r"^[A-Z][a-z]+(( )[A-Z][a-z]+)*$"
    while not re.match(textlookfor,name):
        name = input('Enter valid name')
    return name



def price_validator(price):
    textlookfor = r"^\d+\.\d+$"
    while not re.match(textlookfor,str(price)):
        price = input('Enter valid price')
    return price


def bed_type_validator(bed_type):
    textlookfor = r"^[A-Z][a-z]+(( )[A-Z][a-z]+)*$|^[A-Z][a-z]+[-][a-z]+ [A-Z][a-z]+$"
    while not re.match(textlookfor,bed_type):
        bed_type = input('Enter valid bed_type')
    return bed_type




