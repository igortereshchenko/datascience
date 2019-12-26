import re


def key_valid(var):
    regexp = re.compile(r"^[A-Z]{1}[a-z]+$")
    text = input(var)
    while not bool(regexp.match(text)):
        text=input(var)
    return text

print(key_valid('input zip_city: '))


def spc_valid(var1):
    regexp = re.compile(r"^[A-Za-z\s]+$")
    text = input(var1)
    while not bool(regexp.match(text)):
        text=input(var1)
    return text
print(spc_valid('input spc_common: '))


def horzgr_valid(var2):
    regexp = re.compile(r"^yes|no$")
    text = input(var2)
    while not bool(regexp.match(text)):
        text=input(var2)
    return text
print(horzgr_valid('input yes or no: '))


def year_valid(var3):
    regexp = re.compile(r"^\d{4}$")
    text = input(var3)
    while not bool(regexp.match(text)):
        text=input(var3)
    return text
print(year_valid('input year: '))