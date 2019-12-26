import re

def boroname_validator(promt):
    pattern = re.compile(r"^[A-Z]{1}\w{1,10}$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

#print(boroname_validator('input boroname : '))

def cb_num_validator(promt):
    pattern = re.compile(r"^0{1}|([1-9]{1}[0-9]{0,})$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

#print(cb_num_validator('input cb_num : '))

def st_accem_validator(promt):
    pattern = re.compile(r"^0{1}|([1-9]{1}[0-9]{0,})$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

#print(st_accem_validator('input st_accem_ : '))

def st_senate_validator(promt):
    pattern = re.compile(r"^0{1}|([1-9]{1}[0-9]{0,})$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

#print(st_senate_validator('input st_senate : '))