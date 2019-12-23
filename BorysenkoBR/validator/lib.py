import re

def city_validator(promt):
    re_city=re.compile("^(\D+[-]?)+$")
    text=input(promt)
    while not bool(re_city.match(text)):
        text = input("Invalid data, try entering the city again")
    return text

def provider_id_validator(promt):
    re_provider_id=re.compile("^\d{6}$")
    text=input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text


def percent_of_beneficiaries_with_osteoporosis_validator(promt):
    re_osteoporosis=re.compile("^\d{1,3}$")
    text=input(promt)
    while not bool(re_osteoporosis.match(text)) or int(text)>100:
        text = input("Invalid data, try entering the percent of beneficiaries with osteoporosis again")
    return text

def percent_of_beneficiaries_with_schizophrenia_validator(promt):
    re_schizophrenia=re.compile("^\d{1,3}$")
    text=input(promt)
    while not bool(re_schizophrenia.match(text)) or int(text) > 100:
        text = input("Invalid data, try entering the percent of beneficiaries with schizophrenia again")
    return text
