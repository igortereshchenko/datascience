from re import *

def vert_wall_validator(inputed_text):
    return inputed_text.lower() in ['no','yes']

def wire_2nd_validator(inputed_text):
    return inputed_text.lower() in ['no','yes']

def cen_year_validator(inputed_text):
        return bool(fullmatch(r'\d{4}', inputed_text))

def tree_loc_validator(inputed_text):
        return inputed_text.lower() in ['assigned','side','median','across','front','adjacent']

