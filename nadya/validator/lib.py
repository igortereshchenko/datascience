import re

def color_validator(prompt):
    color = input(prompt)
    while not bool(re.match('^\w+.\w{0,}$', color)):
        color = input(prompt)
    return color

def brand_validator(prompt):
    brand = input(prompt)
    while not bool(re.match('^\w+.\w{0,}$', brand)):
        brand = input(prompt)
    return brand

def review_validator(prompt):
    review = input(prompt)
    while not bool(re.match('(\w+\s+?)*.', review)):
        review = input(prompt)
    return review

def weight_validator(prompt):
    weight = input(prompt)
    while not bool(re.match("^(\d{1,}\s{0,}.)*$", weight)):
        weight = input(prompt)
    return weight
