from VolosheniukY.integration.dataset_structure_common import data_set
from VolosheniukY.validator.lib import *
from SaltykovAn.validator.lib import *


def add_data(data_s, name, city, country, country_code, room_type, price, weekly_price, beds):
    data_s.update({
        name: {
            "city": city,
            "country": country,
            "country_code": country_code,
            'room_type': room_type,
            'price': price,
            'weekly_price': weekly_price,
            'beds': beds,

        }
    })
    return data_s


functions = [name_validator, city_validator, country_validator, country_code_validator, room_type_validator, price_validator, weekly_price_validator, beds_validator]
properties = ['name', 'city', 'country', 'country code', 'room type', 'price', 'weekly price', 'beds']
data_to_add = []

for i in range(len(functions)):
    text = input('Input ' + properties[i] + '\n')
    correct = False
    while not correct:
        if functions[i](text):
            correct = True
        else:
            text = input("Incorrect data, please try again.\n")
    data_to_add.append(text)


add_data(data_set, *data_to_add)
print(data_set)

