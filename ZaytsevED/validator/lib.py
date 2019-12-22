import re


def provide_id_validator(in_txt):
    while not re.findall('^\d{6}$', in_txt):
        in_txt = input('Input the 6-digit identification number for the home health agency: ')
    return in_txt


def state_validator(in_txt):
    while not re.findall('^[A-Z]{2}$', in_txt):
        in_txt = input('Input state where agency is located: ')
    return in_txt


def white_beneficiaries_validator(in_txt):
    while not re.findall('^\d\d*$', in_txt):
        in_txt = input('Input number of non-Hispanic white beneficiaries: ')
    return in_txt


def black_beneficiaries_validator(in_txt):
    while not re.findall('^\d\d*$', in_txt):
        in_txt = input('Input number of non-Hispanic black or African American beneficiaries: ')
    return in_txt
