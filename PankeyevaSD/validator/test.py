
# id_validator = "747429"
# zip_code =  "77459"
# percent_of_beneficiaries_with_copd =  "21"
# percent_of_beneficiaries_with_hypertension =  "67"

import re
def id_validator():
    a = True
    while a:
        id = input('id pls: ')
        if bool(re.match('^\d{6}$',id)):
            a = False
            return id
        else:
            print('Expression is invalid')
def zip_code_validator():
    a = True
    while a:
        zip = input('zip pls: ')
        if bool(re.match('^\d{5}$',zip)):
            a = False
            return zip
        else:
            print('Expression is invalid')
def percent_of_beneficiaries_with_copd_validator():
    a = True
    while a:
        copd = input('copd pls: ')
        if bool(re.match("^([0-9]{1,2})?$",copd)) or bool(re.match('^([1]{1}[0]{1}[0]{1})?$',copd)):
            a = False
            return copd
        else:
            print('Expression is invalid')
def percent_of_beneficiaries_with_hypertension_validator():
    a = True
    while a:
        hypertension = input('hypertension pls: ')
        if bool(re.match("^([1]?[0-9]{1,2})?$",hypertension)):
            a = False
            return hypertension
        else:
            print('Expression is invalid')
id_validator()
zip_code_validator ()
percent_of_beneficiaries_with_hypertension_validator()
percent_of_beneficiaries_with_copd_validator()