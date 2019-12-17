import re


def keys_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^\w+(.com)[/\w]*$", text))


def asins_validator(text: str) -> bool:
    return bool(re.fullmatch(r"^((([A-Z]|[0-9]){10})|(None))?(,([A-Z]|[0-9]){10})*$", text))


#def name_validator(text: str) -> bool:
#    return bool(re.fullmatch(r"^[\w\s,]+$", text))
#Однаково називаються валідатори та пайтон не може визначитися звідки його брати, з мого файлу, чи файлу мого колеги, тому закоментував цей

#def sizes_validator(text: str) -> bool:
#    return bool(re.fullmatch(r"[0-9]*\.?[0-9]*", text))
#Однаково називаються валідатори та пайтон не може визначитися звідки його брати, з мого файлу, чи файлу мого колеги, тому закоментував цей