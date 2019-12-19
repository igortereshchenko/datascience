import re

re_integer = re.compile("^\d+$")
re_names = re.compile("^[A-Z]+$")

def provider_id_validator(provider_id):
    while not re.match(re_integer, provider_id):
        provider_id = input("Введіть будь ласка ідентифікаційний номер правильно: ")
    return provider_id

def agency_name_validator(agency_name):
    while not re.match(re_names, agency_name):
        agency_name = input("Введіть будь ласка назву агенції охорони зворов'я правильному форматі: ")
    return agency_name

def total_lupa_edisodes_validator(total_lupa_edisodes):
    while not re.match(re_integer, total_lupa_edisodes):
            total_lupa_edisodes = input('Введіть будь ласка залну суму платежів правильно: ')
    return total_lupa_edisodes

def avarage_age_validator(avarage_age):
    while not re.match(re_integer, avarage_age):
        avarage_age = input("Введіть будь ласка середній рік правильно: ")
    return avarage_age
