import re
def cb_num_validator(cb_num):
    if bool(re.match(r"^\d+$",cb_num)):
        return True
    else:
        return False

def zipcode_validator(zipcode):
    if bool(re.match(r"^\d+$", zipcode)):
        return True
    else:
        return False
def wire_2nd_validator(wire_2nd):
    if bool(re.match(r"(False)|(True)", wire_2nd)):
        return True
    else:
        return False
def spc_latin_validator(spc_latin):
    if bool(re.match(r"[A-Z]+(\s)[A-Z]+", spc_latin)):
        return True
    else:
        return False
