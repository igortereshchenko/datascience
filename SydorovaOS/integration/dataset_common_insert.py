from SydorovaOS.validator.lib import *
from Matvienko.validator.lib import *
from SydorovaOS.integration.dataset_structure_common import dataset
def circle_input(validator,prompt):
    val = input(prompt)
    while not validator(val):
        val = input(prompt)
    return val
zipcode = int(circle_input(zipcode_validator,"Введіть поштовий індекс "))
status = circle_input(status_validator,"Введіть стан дерева ")
inf_shoes = circle_input(inf_shoes_validator,"Введіть чи наявне взуття ")
trunk_dmg = circle_input(trunk_dmg_validator,"Введіть опис пошкоджень дерева ")
horz_plant = circle_input(horz_plant_validator,"Введіть чи присутні насадження ")
vert_wall = circle_input(vert_wall_validator,"Введіть чи присутнє огородження дерева стіною ")
sidw_raise = circle_input(sidw_raise_validator,"Введіть чи присутній піднятий тротуар ")
cen_year = circle_input(cen_year_validator,"Введіть рік інвентаризації ")

dataset.update({zipcode:{'status':status,'inf_shoes':inf_shoes,'trunk_dmg':trunk_dmg,'horz_plant':horz_plant,'vert_wall':vert_wall,'sidw_raise':sidw_raise,'cen_year':cen_year}})
print(dataset)