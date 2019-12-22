import re

def id_validator(prompt):
    id = input(prompt)
    while not bool(re.match('^AVpe.{16}$', id)):
        id = input(prompt)
    return str(id)

def name_validator(prompt):
    name = input(prompt)
    while not bool(re.match('^\w+.+$', name)):
        name = input(prompt)
    return str(name)

def price_amountMin_validator(prompt):
    price = input(prompt)
    while not bool(re.match('^\d*\.?\d*$', price)):
        price = input(prompt)
    return str(price)

def sizes_validator(prompt):
    sizes = input(prompt)
    while not bool(re.match('^((\d*\.?\d*)|(None))?(,\d*\.?\d*)*$', sizes)):
        sizes = input(prompt)
    return str(sizes)