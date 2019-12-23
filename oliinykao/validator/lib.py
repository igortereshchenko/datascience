import re
def id_validator(prompt):
    id = input(prompt)
    while not bool(re.match("^AVpe.{16}$", id)):
        id = input(prompt)
    return id

def brand_validator(prompt):
    brand = input(prompt)
    while not bool(re.match("^\w*(\s\w*)*$", brand)):
        brand = input(prompt)
    return brand

def colors_validator(prompt):
    colors = input(prompt)
    while not bool(re.match("^\w*(.?\s\w*)*$", colors)):
        colors = input(prompt)
    return colors

def flavors_validator(prompt):
    flavors = input(prompt)
    while not bool(re.match("^\w*(\s\w*)*$", flavors)):
        flavors = input(prompt)
    return flavors