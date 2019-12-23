from LutakMV.validator.lib import *
from danylenkoka.validator.lib import *
from LutakMV.dataset_structure import dt
def add_inf(validator, prompt):
    text = input(prompt)
    while not validator(text):
        text = input(prompt)
    return text


st_assem = add_inf(st_assem_validator, 'Введіть код вулиці: ')
spc_latin = add_inf(spc_latin_validator, 'Введіть наукову назву рослини: ')
inf_canopy = add_inf(inf_canopy_validator, 'Чи накрите дерево при перевезенні: ')
zipcode = add_inf(zipcode_validator, 'Введіть поштовий індекс, куди прибудуть дерева: ')
vert_wall = add_inf(vert_wall_validator, 'Чи наявна деревна стіна: ')
wire_2nd = add_inf(wire_2nd_validator, 'Чи наявні вторинні проводи: ')
cen_year = add_inf(cen_year_validator, 'Введіть рік іннвентаризації дерева: ')

dt.update({st_assem: {spc_latin : {'inf_canopy': inf_canopy, 'zipcode': zipcode, 'vert_wall': vert_wall, 'wire_2nd': wire_2nd, 'cen_year': cen_year}}})
print(dt)