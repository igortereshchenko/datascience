import re


def horz_plant_validator(arg):
    return bool(re.fullmatch('(Yes)|(No)', arg))


def wire_other_validator(arg):
    return bool(re.fullmatch('(Yes)|(No)', arg))


def borocode_validator(arg):
    return bool(re.fullmatch('[1-5]', arg))


def status_validator(arg):
    return bool(re.fullmatch('(Good)|(Excellent)|(Dead)|(Poor)', arg))
