import re


def provider_id_validator(text):
    match = re.match('^\d{1,6}$', text)
    if match:
        return True
    else:
        print(f'\'{text}\' is not valid, must be up to 6 digits!')
        return False


def city_validator(text):
    match = re.match('[A-Z\s]+', text)
    if match:
        return True
    else:
        print(f'\'{text}\' is not valid, must be capital word(-s)!')
        return False


def zip_code_validator(text):
    match = re.match('^\d{5}$', text)
    if match:
        return True
    else:
        print(f'\'{text}\' is not valid, must be 5 digits!')
        return False


def total_episodes_non_lupa_validator(text):
    match = re.match('\d+', text)
    if match:
        return True
    else:
        print(f'\'{text}\' is not valid, must be integer!')
        return False


def percent_of_beneficiaries_with_ra_oa_validator(data):
    match = re.match(r'^(10)?0$|^[1-9][0-9]?$', data)
    if match:
        return True
    else:
        print(f'\'{data}\' is not valid, must be integer from 0 to 100!')
        return False


def percent_of_beneficiaries_with_stroke_validator(data):
    match = re.match(r'^(10)?0$|^[1-9][0-9]?$', data)
    if match:
        return True
    else:
        print(f'\'{data}\' is not valid, must be integer from 0 to 100!')
        return False
