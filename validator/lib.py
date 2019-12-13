import re

def name_validator(name):
    while not re.match('^\w+$', name):
        name = input("Введіть ім'я у правильному форматі: ")
    return name
def weight_validator(weight):
    while not re.match(("^[-+]{0,1}\d+$"), weight):
        weight = input("Введіть вагу товару у правильному форматі: ")
    return weight + " kg"

def brand_validator(brand):
    while not re.match('^[A-z]*$', brand):
            brand=input('Введіть назву бренду у правильному форматі: ')
    return brand

def dimension_validator(dimension):
    while not re.match(("^[-+]{0,1}\d+$"), dimension):
        dimension = input("Введіть розмір у правильному форматі: ")
    return dimension