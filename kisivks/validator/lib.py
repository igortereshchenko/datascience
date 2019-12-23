import re


def provider_id_validator(data):
    match = re.fullmatch(r'[0-9]{6}', data)
    return match is not None


def zip_code_validator(data):
    match = re.fullmatch(r'[0-9]+', data)
    return match is not None


def percent_of_beneficiaries_with_ra_oa_validator(data):
    match = re.fullmatch(r'^100$|^[1-9]?[0-9]$', data)
    return match is not None


def percent_of_beneficiaries_with_stroke_validator(data):
    match = re.fullmatch(r'^100$|^[1-9]?[0-9]$', data)
    return match is not None
