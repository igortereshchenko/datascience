import re
def validator_of_id(id):
    return bool(re.match(r'^\d+$',id))

def validator_of_neighbourhood(neighbourhood):
    return bool(re.match(r'^(\b[A-Z]{1}[a-z]+\b\s*)*$',neighbourhood))

def validator_of_state(state):
    return bool(re.match(r'^(\b[A-Z]+[a-z]*\b\s*)*$',state))

def validator_of_market(market):
    return bool(re.match(r'^(\b[A-Z]{1}[a-z]+\b\s*)*$',market))

def validator_of_country(country):
    return bool(re.match(r'^(\b[A-Z]*[a-z]*\b\s*)*$',country))