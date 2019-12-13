
import re
def count_validator(count):
    while not re.match('^[1-9]{1}[0-9]*$',count) :
        count = input('enter correct count \n')
    return count


def name_validator(name):
    while not re.match('^[A-Z]{1}[a-z]*$',name) :
        name = input('enter correct name \n')
    return name


def reviews_validator(reviews):
    while not re.match('^[1-9]{1}[0-9]*$',reviews) :
        reviews = input('enter correct reviews \n')
    return reviews
def td_validator(td):
    while not re.match('^[0-9 a-z A-Z]*$',td) :
        td = input('enter correct reviews \n')
    return td