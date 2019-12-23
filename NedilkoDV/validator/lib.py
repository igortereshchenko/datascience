import re
from NedilkoDV.dataset_structure import dataset



def ID_validator(ID):
    while not re.match('^([a-zA-Z\d(\-)(\_)])*$', ID):
        ID=input('Введіть id у правильному форматі')
    return ID

def count_validator(num):
    while not re.match('\d', num):
        num=input('Введіть кількість у правильному форматі')
    return int(num)


def key_validator(key):
    while not re.match('([A-z]+\s{0,1})+', key):
            key=input('Введіть УСІ властивості у правильному форматі')
    return key
def brand_validator(brand):
    while not re.match('^[A-z]*$', brand):
            brand=input('Введіть фірму у правильному форматі')
    return brand