import re


def spc_common_validator(text: str) -> bool:
    text = text.replace(" ", "")
    return bool(re.fullmatch(r"^[\w,][^0-9]+$", text))


def inf_other_validator(text: str) -> bool:
    return text.lower() in ["yes", "no"]


def cen_year_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^\d{4}$", text))


def zip_city_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^[\w,\s][^0-9]+$", text))
