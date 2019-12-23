import re

def provider_id_validator(promt):
    re_provider_id=re.compile("^\d{6}$")
    text=input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text

def city_validator(promt):
    re_provider_id=re.compile("^\w+$")
    text=input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text

def percent_of_beneficiaries_with_cancer_validator(promt):
    re_provider_id=re.compile("^\d{1,2}$")
    text=input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text

def percent_of_beneficiaries_with_diabetes_validator(promt):
    re_provider_id=re.compile("^\d{1,2}$")
    text=input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text