import re


def validator(prompt_input, prompt_error, pattern):
    text = input(prompt_input).replace(" ", "")
    while not bool(pattern.match(text)):
        text = input(prompt_error).replace(" ", "")
    return text


def provider_id_validator():
    return validator('Please input Provider ID: ', 'Sorry, provider ID must consist of 6 numbers. Try again: ',
                     re.compile("\s*\d{6}\s*"))


def state_validator():
    return validator('Please input state: ', 'Please input state abbreviation. Try again: ',
                     re.compile("\s*\w{2}\s*")).upper()


def percent_of_beneficiaries_with_depression_validator():
    value = validator('Please input percent of beneficiaries with depression: ',
                      'Percent must be a number between 0 and 100. Try again: ',
                      re.compile("\s*\d{1, 3}\s*"))
    while float(value) < 0 or float(value) > 100:
        print('Percent can not be higher than 100 or lower than 0.')
        value = validator('Please input percent of beneficiaries with depression: ',
                          'Percent must be a number between 0 and 100. Try again: ',
                          re.compile("\s*\d{1, 3}\s*"))
    return value


def percent_of_beneficiaries_with_hyperlipidemia_validator():
    value = validator('Please input percent of beneficiaries with hyperlipidemia: ',
                      'Percent must be a number between 0 and 100. Try again: ',
                      re.compile("\s*\d{1, 3}\s*"))
    while float(value) < 0 or float(value) > 100:
        print('Percent can not be higher than 100 or lower than 0.')
        value = validator('Please input percent of beneficiaries with hyperlipidemia: ',
                          'Percent must be a number between 0 and 100. Try again: ',
                          re.compile("\s*\d{1, 3}\s*"))
    return value
