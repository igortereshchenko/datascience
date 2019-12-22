import re

def host_name_validator(data,key,value):
    v = re.compile(r'\b' + key + r'\b')
    if v.search(str(list(data.keys()))):
        data[key] = value
        return data
    else:
        print('no key in data')
        return data

def host_identity_validator(data,key,atribute,value):
    check_atribute = 'host_identity'
    v = re.compile(r'\b' + key + r'\b')
    b = re.compile(atribute)
    if v.search(str(list(data.keys()))):
        if b.search(check_atribute):
            data[key][atribute] = value
            return data
        else:
            print('no atribute in data')
            return data
    else:
        print('no key in data')
        return data

def host_is_superhost_validator(data,key,atribute,value):
    check_atribute = 'host_is_superhost'
    v = re.compile(r'\b' + key + r'\b')
    b = re.compile(atribute)
    if v.search(str(list(data.keys()))):
        if b.search(check_atribute):
            data[key][atribute] = value
            return data
        else:
            print('no atribute in data')
            return data
    else:
        print('no key in data')
        return data

def street_validator(data,key,atribute,value):
    check_atribute = 'street'
    v = re.compile(r'\b' + key + r'\b')
    b = re.compile(atribute)
    if v.search(str(list(data.keys()))):
        if b.search(check_atribute):
            data[key][atribute] = value
            return data
        else:
            print('no atribute in data')
            return data
    else:
        print('no key in data')
        return data