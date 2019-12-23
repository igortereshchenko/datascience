import re


def host_identity_validator(data, key_first_priority, key_second_priority, atribute, value):
    check_atribute = 'host_identity'
    b = re.compile(r'^' + atribute + r'$')
    if b.match(check_atribute):
        data[key_first_priority][key_second_priority][atribute] = value
    return data



def host_is_superhost_validator(data, key_first_priority, key_second_priority, atribute, value):
    check_atribute = 'host_is_superhost'
    b = re.compile(r'^' + atribute + r'$')
    if b.match(check_atribute):
        data[key_first_priority][key_second_priority][atribute] = value
    return data


def street_validator(data, key_first_priority, key_second_priority, atribute, value):
    check_atribute = 'street'
    b = re.compile(r'^' + atribute + r'$')
    if b.match(check_atribute):
        data[key_first_priority][key_second_priority][atribute] = value
    return data

def neighbourhood_validator(data, key_first_priority, key_second_priority, atribute, value):
    check_atribute = 'neighbourhood'
    b = re.compile(r'^' + atribute + r'$')
    if b.match(check_atribute):
        data[key_first_priority][key_second_priority][atribute] = value
    return data

def state_validator(data, key_first_priority, key_second_priority, atribute, value):
    check_atribute = 'state'
    b = re.compile(r'^' + atribute + r'$')
    if b.match(check_atribute):
        data[key_first_priority][key_second_priority][atribute] = value
    return data

def market_validator(data, key_first_priority, key_second_priority, atribute, value):
    check_atribute = 'market'
    b = re.compile(r'^' + atribute + r'$')
    if b.match(check_atribute):
        data[key_first_priority][key_second_priority][atribute] = value
    return data

def country_validator(data, key_first_priority, key_second_priority, atribute, value):
    check_atribute = 'country'
    b = re.compile(r'^' + atribute + r'$')
    if b.match(check_atribute):
        data[key_first_priority][key_second_priority][atribute] = value
    return data