import re
city_validator = r"[\w{2,167}]"
nta_name_validator = r"\w+{2,167}"
code_validator = r"\d{6}"
borocode_validator = r"[1-5]{1}"
cb_num_validator = r"\d{1}"


def code_request():
    user_input = input("Input code (6-7 numbers) : ")
    while not re.match(code_validator, user_input):
        user_input = input("Input code (6-7 numbers) : ")
    return str(user_input)


def zip_city_request():
    user_input = input("Input city name : ")
    while not re.match(city_validator, user_input):
        user_input = input("Input city name : ")
    return str(user_input)


def borocode_request():
    user_input = input("Input borocode (from 1 to 5) : ")
    while not re.match(borocode_validator, user_input):
        user_input = input("Input borocode (from 1 to 5) : ")
    return str(user_input)


def nta_name_request():
    user_input = input("Input nta_name : ")
    while not re.match(nta_name_validator, user_input):
        user_input = input("Input nta_name : ")
    return str(user_input)


def cb_num_request():
    user_input = input("Enter nta_name : ")
    while not re.match(cb_num_validator, user_input):
        user_input = input("Enter nta_name : ")
    return str(user_input)
