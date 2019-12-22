import re
def zip_city_validator(zip_city):
    if bool(re.match(r"[A-Z][a-z]+",zip_city)):
        return True
    else:
        return False

def st_assem_validator(st_assem):
    if bool(re.match(r"[01]", st_assem)):
        return True
    else:
        return False
def horz_blck_validator(horz_blck):
    if bool(re.match(r"(Yes)|(No)|(yes)|(no)", horz_blck)):
        return True
    else:
        return False
def sen_year_validator(sen_year):
    if bool(re.match(r"^\d{4}$", sen_year)):
        return True
    else:
        return False