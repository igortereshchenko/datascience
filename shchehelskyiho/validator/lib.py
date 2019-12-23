import re

def zipcode_validator(zipcode):
    return True if re.match(r'^\d+$', zipcode) else False

def street_validator(street):
    return True if re.match(r'^[\w\,\-\/\\\s]+$', street) else False

def space_validator(space):
    return True if re.match(r'^.*$', space) else False

def host_id_validator(host_id):
    return True if re.match(r'^\d+$', host_id) else False