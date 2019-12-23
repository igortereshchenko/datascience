import re

def  inf_canopy_validator(check_str):
    return bool(re.match(r"^(Yes)$|^(No)$", check_str))

def  inf_shoes_validator(check_str):
    return bool(re.match(r"^(Yes)$|^(No)$", check_str))

def  zip_city_validator(check_str):
    return bool(re.match(r"^[A-Z]\w+(\s[A-Z]\w+)?$", check_str))

def  cb_num_validator(check_str):
    return bool(re.match(r"^[0-5]?[0-9]{0,2}$", check_str))

# def inf_canopy_validator(temp_str=""):
#     while not is_yes_no(temp_str):
#         temp_str = input()
#     return temp_str
#
# def inf_shoes_validator():
#     temp_str = input()
#     while not is_yes_no(temp_str):
#         temp_str = input()
#     return temp_str
#
# def zip_city_validator():
#     temp_str = input()
#     while not is_city(temp_str):
#         temp_str = input()
#     return temp_str
#
# def cb_num_validator():
#     temp_str = input()
#     while not is_cb_num(temp_str):
#         temp_str = input()
#     return int(temp_str)
