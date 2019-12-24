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
def state_validator(txt):
    pattern = re.compile('([A-Z])([A-Z])')
    if re.match(pattern, txt):
        return True
    else:
        print('It is not a state')
        return False


def percent_of_beneficiaries_with_cancer_validator(txt):
    pattern = re.compile(r'100|\d?\d+')
    if re.match(r'100|\d?\d', txt) and float(txt) <= 100:
        return True
    else:
        print('It can\'t be a percent_of_beneficiaries_with_cancer')
        return False


def percent_of_beneficiaries_with_depression_validator(txt):
    if re.match(r'100|\d?\d', txt) and float(txt) <= 100:
        return True
    else:
        print('It can\'t be a percent_of_depression_with_depression')
        return False

def provider_id_validator (txt):
    if re.match(r'\d\d\d\d\d\d', txt):
        return True
    else:
        print('It can\'t be a provider_id')
        return False
