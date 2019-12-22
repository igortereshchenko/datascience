import re

def zip_code_validator(promt):
    re_zip=re.compile("^\d+$")
    text=input(promt)
    while not bool(re_zip.match(text)):
        text = input("Invalid data, try entering the zip_code again")
    return text

def provider_id_validator(promt):
    re_provider_id=re.compile("^\d+$")
    text=input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text

def distinct_beneficiaries_non_lupa_validator(promt):
    re_lupa=re.compile("^\d+$")
    text=input(promt)
    while not bool(re_lupa.match(text)):
        text = input("Invalid data, try entering the percent of beneficiaries with lupa again")
    return text

def average_number_of_total_visits_per_episode_non_lupa_validator(promt):
    re_non_lupa=re.compile("^\d+$")
    text=input(promt)
    while not bool(re_non_lupa.match(text)):
        text = input("Invalid data, try entering the percent of beneficiaries with non_lupa again")
