import re


def spc_latin_validator(text: str):
    text = text.replace(" ", "")
    if bool(re.fullmatch(r"^[\w,][^0-9]+$", text)):
        return text


def wire_htap_validator(text: str):
    if bool(re.fullmatch(r"^(yes|no)$", text)):
        return text


def status_validator(text: str):
    if bool(re.fullmatch(r"^(excellent|bad|good|dead|poor)$", text)):
        return text


def borocode_validator(text: str):
    if bool(re.fullmatch(r"^\d$", text)):
        return text