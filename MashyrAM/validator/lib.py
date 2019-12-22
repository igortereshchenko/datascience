import re

def provider_id_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^\d{6}$", text))

def city_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^[A-Z]{2,}$", text))

def percent_of_beneficiaries_with_hypertension_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^\d{1,2} ", text))

def  percent_of_beneficiaries_with_osteoporosis_validator(text: str) -> bool:
    return bool(re.fullmatch(r"\d{1,2} ", text))