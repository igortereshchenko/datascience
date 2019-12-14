
def state_validator(txt):
    pattern = re.compile('([A-Z])([A-Z])')
    if re.match(pattern, txt):
        return txt
    else:
        print('It is not a state')


def percent_of_beneficiaries_with_cancer_validator(txt):
    pattern = re.compile('(1)*\d*\d+')
    if re.match(pattern, txt):
        return txt
    else:
        print('It can\'t be a percent_of_beneficiaries_with_cancer')


def percent_of_beneficiaries_with_depression_validator(txt):
    pattern = re.compile('(1)*\d*\d+')
    if re.match(pattern, txt):
        return txt
    else:
        print('It can\'t be a percent_of_depression_with_cancer')
