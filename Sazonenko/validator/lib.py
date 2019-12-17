import re


def spc_latin_validator(text: str) -> bool:
    text = text.replace(" ", "")
    return bool(re.fullmatch(r"^[\w,][^0-9]+$", text))


def wire_htap_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^(yes|no)$", text))


def status_validator(text: str) -> bool:

    return bool(re.fullmatch(r"^(excellent|bad|good|dead|poor)$", text))


def borocode_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^\d$", text))