import re

"""
Validators for each attribute. 
Function name form: name_of_attribute_validator
"""

def id_validator(id):
    return re.match("^[0-9]{6}$", id)

def agency_name_validator(agency_name):
    return re.match("^(([A-Z]+)\s)+([A-Z]+\,\s(INC)(\s[A-Z]+)*)$", agency_name)

def street_adress_validator(street_adress):
    return re.match("^[0-9]+\s(([A-Z]+)\s)+([A-Z]+)$", street_adress)

def city_validator(city):
    return re.match("^([A-Z][\s\-]?)*[A-Z]$", city) 
