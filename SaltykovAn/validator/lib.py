import re


def room_type_validator(room_type):
    return bool(re.match("^[A-Z][a-z]+(( |/)[a-z]+)+$", room_type))


def price_validator(price):
    return bool(re.match("^((\d+\.\d+)|\d+)$", price))


def weekly_price_validator(weekly_price):
    return bool(re.match("^((\d+.\d+)|\d+)$", weekly_price))


def beds_validator(beds):
    return bool(re.match("^(\d+)$", beds))