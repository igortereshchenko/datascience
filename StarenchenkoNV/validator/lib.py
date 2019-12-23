import re

num_regexp = re.compile(r"^\d+$")
str_regexp = re.compile(r"^Yes|No$")


def is_something(pattern, text):

    return bool(pattern.match(text))


def wire_prime_validator(str_regexp):

    wire_prime_status = input("Please enter 'Yes' or 'No' to discribe satus of prime wires: ")

    while not is_something(str_regexp, wire_prime_status):
        print("please enter one of given variants!")
        wire_prime_status = input("Please enter 'Yes' or 'No' to discribe status of prime wires: ")
    return wire_prime_status


def inf_shoes_validator(str_regexp):

    shoes_status = input("Please enter 'Yes' or 'No' to discribe presentece of sneakers: ")

    while not is_something(str_regexp, shoes_status):
        print("please enter one of given variants!")
        shoes_status = input("Please enter 'Yes' or 'No' to discribe presentece of sneakers: ")
    return shoes_status


def sidw_crack_validator(str_regexp):

    sidw_crack_status = input("Please enter 'Yes' or 'No' to discribe status of sidewalk cracks: ")

    while not is_something(str_regexp, sidw_crack_status):
        print("please enter one of given variants!")
        sidw_crack_status = input("Please enter 'Yes' or 'No' to discribe status of sidewalk cracks: ")
    return sidw_crack_status


def cb_num_validator(num_regexp):

    cb_num = input("enter number of district: ")

    while not is_something(num_regexp, cb_num):
        print("please enter a number! \n")
        cb_num = input("enter number of district: ")
    return cb_num


