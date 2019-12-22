import re
re_objectid = re.compile("[\d]{6}$")
re_vert_wall = re.compile("^Yes|No")
re_zipcode = re.compile("[\d]{5}$")
re_borocode = re.compile("[1, 2, 3, 4, 5]{1}$")


def checking(pattern, x):
    return bool(pattern.match(x))


def objectid_validator(pattern, values):
    text = input(values)
    while not checking(pattern, text):
        text = input(values)
    return int(text)


def vert_wall_validator(pattern, values):
    text = input(values)
    while not checking(pattern, text):
        text = input(values)
    return str(text)


def zipcode_validator(pattern, values):
    text = input(values)
    while not checking(pattern, text):
        text = input(values)
    return int(text)


def borocode_validator(pattern, values):
    text = input(values)
    while not checking(pattern, text):
        text = input(values)
    return int(text)



