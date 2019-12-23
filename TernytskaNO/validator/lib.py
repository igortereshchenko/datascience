import re

def spc_latin_validator(text):
    return bool(re.match(r"^[A-Z][a-z]+(\s[A-Z][a-z]+)?$", text))

def status_validator(text):
    return bool(re.match(r"^(excellent)$|^(good)$|^(poor)$|^(dead)$",text))

def cen_year_validator(text):
    return bool(re.match(r"^\d{4}$",text))

def  wire_prime_validator(text):
    return bool(re.match(r"^(Yes)$|^(No)$", text))