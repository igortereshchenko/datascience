import re


def zip_city_request(input: str):
    return bool(re.fullmatch(r"([A-Z]+\s*)+", input))


def boroname_request(input: str):
    return bool(re.fullmatch(r"([A-Z]+\s*)+", input))


def borocode_request(input: str):
    return bool(re.fullmatch(r"[1-5]", input))


def cb_num_request(input: str):
    return bool(re.fullmatch(r"\d", input))
