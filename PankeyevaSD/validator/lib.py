import re
def id_validator(id):
   return bool(re.match('^\d{6}$',id))


def zip_code_validator(zip):
    return bool(re.match('^\d{5}$', zip))


def percent_of_beneficiaries_with_copd_validator(copd):
   return bool(re.match('^([0-9]{1,2})?$',copd)) or bool(re.match('^([1]{1}[0]{1}[0]{1})?$',copd))


def percent_of_beneficiaries_with_hypertension_validator(hypertension):
    return bool(re.match('^([1]?[0-9]{1,2})?$', hypertension))
