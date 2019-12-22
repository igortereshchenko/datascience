from PindaMV.validator.lib import *
from PindaMV.integration.validator_lib_andrey import *
from PindaMV.integration.dataset_structure_common import dataset

def common_validator(prompt, validator):
    var = input(prompt)
    while not validator(var):
        var = input(prompt)
    return var

latin = common_validator('Введіть латинську назву дерева: ', spc_latin_validator)

year = int(common_validator('Введіть рік: ', cen_year_validator))
wire = common_validator('Наявні дроти? ', wire_other_validator)
inf = common_validator('Наявні конфлікти з інфраструктурою? ', inf_other_validator)
zip_city = common_validator('Введіть місто: ', zip_city_validator)
cb = int(common_validator('Введіть номер громадської ради: ', cb_num_validator))
code = int(common_validator('Введіть код міста: ', borocode_validator))
b_name = common_validator('Введіть район, де знаходиться дерево: ', boroname_validator)


def add_row(latin, year, wire, inf, zip_city, cb, code, b_name):
    dataset.update({latin: {year: {'wire_other': wire, 'inf_other': inf, 'zip_city': zip_city,
                                   'cb_num': cb, 'borocode':code,'boroname': b_name}}})
    return dataset

print(add_row(latin, year, wire, inf, zip_city, cb, code, b_name))
