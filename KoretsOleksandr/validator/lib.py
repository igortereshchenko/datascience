import re

def cen_year_validator(promt):
    pattern = re.compile(r"^\d{4}$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def vert_other_validator(promt):
    pattern = re.compile(r"^yes|no$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def borocode_validator(promt):
    pattern = re.compile(r"^[1-5]{1}$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def key_validator(promt):
    pattern = re.compile(r"^[A-Z]{1}\w{1,10}$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text