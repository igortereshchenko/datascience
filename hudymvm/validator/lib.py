import re

def id_validator(prompt):
    id = input(prompt)
    if bool(re.match('AVpe_{1}[-_A-Za-z0-9]{15}', id))!=True:
        id = input(prompt)
    return id

def categories_validator(prompt, sep=","):
    categories = input(prompt)
    if bool(re.match("(([A-Z]{1}[a-z`' ]{1,}\,{0,1}){1,}|(none|None))", categories))!=True:
        categories = input(prompt)
    if isinstance(categories,str):
        categories = categories.split(sep)
    return categories

def keys_validator(prompt, sep=','):
    keys = input(prompt)
    if bool(re.match('([a-z\/,.0-9]{1,}|(none|None))', keys))!=True:
        keys = input(prompt)
    if isinstance(keys,str):
        keys = keys.split(sep)
    return keys

def name_validator(prompt):
    name = input(prompt)
    if bool(re.match("(([A-Z]{1}[A-Za-z'().,/-0-9 ]{1,}\s{0,1}){1,}|(none|None))",name))!=True:
        name = input(prompt)
    return name
