import re


def country_validator(country):

    textlookfor = r"[A-Z][a-z]{5}\s[A-Z][a-z]{5}"
    result = re.match(textlookfor,country)
    return bool(result)



def name_validator(name):
    textlookfor = r"^[A-Z][a-z]+(( )[A-Z][a-z]+)*$"
    result = re.match(textlookfor,name)
    return bool(result)



def price_validator(price):
    textlookfor = r"^\d+\.\d+$"
    result = re.match(textlookfor,str(price))
    return bool(result)


def bed_type_validator(bed_type):
    textlookfor = r"^[A-Z][a-z]+(( )[A-Z][a-z]+)*$|^[A-Z][a-z]+[-][a-z]+ [A-Z][a-z]+$"
    result = re.match(textlookfor,bed_type)
    return bool(result)





