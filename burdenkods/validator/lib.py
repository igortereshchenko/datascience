import re


def keys_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^\w+(.com)[/\w]*$", text))


def asins_validator(text: str) -> bool:
    return text == ""


def name_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^[\w\s,]+$", text))


def sizes_validator(text: str) -> bool:
    return bool(re.fullmatch(r"[0-9]*\.?[0-9]*", text))