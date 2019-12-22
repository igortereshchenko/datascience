from re import match


def id_validator(id):
    return bool(match('^([a-zA-Z\d(\-)(\_)])*$',id))


def ean_validator(ean):
    return bool(match('^\d*$',ean))


def color_validator(color):
    return bool(match('^[A-Z]{0,1}[a-z]*$',color))


def flavor_validator(flavor):
    return bool(match('^[A-Z]{0,1}[a-z]*$',flavor))











