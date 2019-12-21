from lib import *

name = input("Input hotel name\n")
correct = False
while not correct:
    if name_validator(name):
        correct = True
    else:
        name = input("Incorrect data, please try again.\n")


city = input("Input city name\n")
correct = False
while not correct:
    if city_validator(city):
        correct = True
    else:
        city = input("Incorrect data, please try again.\n")


country = input("Input country name\n")
correct = False
while not correct:
    if country_validator(country):
        correct = True
    else:
        country = input("Incorrect data, please try again.\n")


country_code = input("Input country code\n")
correct = False
while not correct:
    if country_code_validator(country_code):
        correct = True
    else:
        country_code = input("Incorrect data, please try again.\n")

