import re
def name_validator(name):
    if re.match('\w*', name):
        return True
    else: return False

def id_validator(id):
    if re.match('^\w*\d*$', id):
        return True
    else: return False

def prices_offer_validator(prices_offer):
    if re.match('^\d*$', prices_offer):
        return True
    else: return False

def size_validator(size):
    if re.match('^\d*$', size):
        return True
    else: return False