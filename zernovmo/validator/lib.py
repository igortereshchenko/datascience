import pycountry

countries = (i.name for i in list(pycountry.countries))


def host_location_validator(host_location):
    if isinstance(host_location, str) and host_location in countries:
        return True
    else:
        return False


def host_is_superhost_validator(host_is_superhost):
    if isinstance(host_is_superhost, bool):
        return True
    else:
        return False


def street_validator(street):
    countries = (i.name for i in list(pycountry.countries))
    if isinstance(street, str) and street in countries:
        return True
    else:
        return False


def host_name_validator(host_name):
    if isinstance(host_name, str):
        return True
    else:
        return False
