import re
def id_validator(id):
    return bool(re.match("^AVpe\_.{15}$", id))

def brand_validator(brand):
    return bool(re.match("^\w*(\s\w*)*$", brand))

def colors_validator(colors):
    return bool(re.match("^\w*(.?\s\w*)*$", colors))

def flavors_validator(flavors):
    return bool(re.match("^\w*(\s\w*)*$", flavors))