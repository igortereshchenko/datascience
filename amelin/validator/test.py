import re

dataset = {
    'Maija' :
        {
        'host_identity': 'true',
        'host_is_superhost': 'false',
        'street': 'Gilman Dr W, Seattle, WA 98119, United States'
        },

    'Andrea' :
        {
        'host_identity': 'true',
        'host_is_superhost': 'true',
        'street': '7th Avenue West, Seattle, WA 98119, United States'
        },

    'Jill' :
        {
        'host_identity': 'true',
        'host_is_superhost': 'true',
        'street': 'West Lee Street, Seattle, WA 98119, United States'
        }
        }

def host_name_validator(data,key,value):
    v = re.compile(r'\b' + key + r'\b')
    if v.search(str(list(data.keys()))):
        data[key] = value
        return data
    else:
        print('no key in data')
        return data


### перший варіант для вводу користувача, другій для тесту програми, можна закоментувати візов функціі з інпутами для легшої перевірки
print(host_name_validator(dataset,input('vvedite key'),input('vvedite value')))
print(host_name_validator(dataset,'Maija','10'))


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


### перший варіант для вводу користувача, другій для тесту програми, можна закоментувати візов функціі з інпутами для легшої перевірки
print(host_identity_validator(dataset, input('vvedite key'), input('vvedite atribut'), input('vvedite value')))
print(host_identity_validator(dataset, 'Maija', 'host_identity', '10'))


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


### перший варіант для вводу користувача, другій для тесту програми, можна закоментувати візов функціі з інпутами для легшої перевірки
print(host_is_superhost_validator(dataset, input('vvedite key'), input('vvedite atribut'), input('vvedite value')))
print(host_is_superhost_validator(dataset, 'Maija', 'host_is_superhost', '10'))


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

### перший варіант для вводу користувача, другій для тесту програми, можна закоментувати візов функціі з інпутами для легшої перевірки
print(street_validator(dataset,input('vvedite key'),input('vvedite atribut'),input('vvedite value')))
print(street_validator(dataset, 'Maija', 'street', '10'))
