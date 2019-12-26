import re


def validator(prompt_input, prompt_error, pattern):
    text = input(prompt_input).replace(" ", "")
    while not bool(pattern.match(text)):
        text = input(prompt_error).replace(" ", "")
    return text


def provider_id_validator():
    return validator('Please input Provider ID: ', 'Sorry, provider ID must consist of 6 numbers. Try again: ',
                     re.compile("\s*\d{6}\s*"))



def agency_name_validator():
    return validator('Please input agency name: ', 'Please input name of hospital. Try again: ',
                     re.compile("\s*\D\s*"))



def male_beneficiaries_validator():
    value = validator('Please input number of male beneficiaries: ',
                      'Number must be more than 0. Try again: ',
                      re.compile("\s*\d\s*"))
    while int(value) < 0:
        print('Number can`t be less than zero')
        value = validator('Please input number of male beneficiaries:: ',
                          'Number must be more than 0. Try again: ',
                          re.compile("\s*\d\s*"))
    return value



def female_beneficiaries_validator():
    value = validator('Please input number of female beneficiaries: ',
                      'Number must be more than 0. Try again: ',
                      re.compile("\s*\d\s*"))
    while int(value) < 0:
        print('Number can`t be less than zero')
        value = validator('Please input number of female beneficiaries:: ',
                          'Number must be more than 0. Try again: ',
                          re.compile("\s*\d\s*"))
    return value

