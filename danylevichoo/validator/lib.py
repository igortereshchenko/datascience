import re

def host_id_validator(host_id_in):
    host_id=input(host_id_in)
    while not re.match('^[+]?\d+$', host_id):
        host_id=input("Enter valid host-id: ")
    return host_id

def bed_type_validator(bed_in):
    bed=input(bed_in)
    while not re.match('^Real Bed$', bed) and not re.match('^Futon$', bed) and not re.match('^Pull-out Sofa$', bed):
        bed=input("Enter valid bed-type (variants)\nReal Bed\nFuton\nPull-out Sofa: ")
    return bed

def price_validator(price_in):
    price=input(price_in)
    while not re.match('^[+]?\d+[.]?\d{,2}$', price):
        price=input("Enter valid price: ")
    return price

def extra_people_validator(extra_in):
    extra=input(extra_in)
    while not re.match('^[+]?\d+[.]?\d{,2}$', extra):
        extra=input("Enter valid extra-price:")
    return extra