import re
def id_validator(prompt):
    id = input(prompt)
    while not bool(re.match("^AVpe.{16}$", id)):
        id = input(prompt)
    return str(id)
def dimension_validator(prompt):
    dimension = input(prompt)
    while not bool(re.match("^\d+\.\d+\sin(\sx\s\d+\.\d+\sin){2}$", dimension)):
        dimension = input(prompt)
    return str(dimension)