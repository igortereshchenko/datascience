import re
def status_validator(my_text):
    lower_text = my_text.lower()
    if lower_text == 'good' or lower_text == 'dead' or lower_text == 'poor' :
        return True
    else:
        return False


def horz_plant_validator(my_text):
    lower_text = my_text.lower()
    if lower_text == 'no' or lower_text == 'yes':
        return True
    else:
        return False


def zip_city_validator(my_text):
    return bool(re.fullmatch(r"^[\w,\s][^0-9]+$", my_text))


def boroname_validator(my_text):
    lower_text = my_text.lower()
    if lower_text == 'bronx' or lower_text == 'queens' or lower_text == '5' or lower_text == 'manhattan' or lower_text == "brooklyn" :
        return True
    else:
        return False
