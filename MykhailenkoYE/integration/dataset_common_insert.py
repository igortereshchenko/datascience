from MykhailenkoYE.validator.lib import *
from LutakMV.validator.lib import *
from MykhailenkoYE.integration.dataset_structure_common import dt_integration
major_name = input("Введіть назву района:")
spc_latin = spc_latin_validator(" Введіть значення spc_latin:")
inf_canopy = boroname_validator("Введіть значення inf_canopy:")
zipcode = zipcode_validator("Введіть значення zipcode:")
st_assem = st_assem_validator("Введіть значення st_assem:")
status = status_validator(input("Введіть значення vert_wall:"))
horz_plant = horz_plant_validator(input("Введіть значення wire_2nd:"))
zip_city = zip_city_validator(input("Введіть значення cen_year:"))
boroname = boroname_validator(input("Введіть значення tree_loc:"))

dt_integration.update({major_name:{'boroname':boroname, 'zip_city': zip_city, 'st_assem': st_assem, 'horz_plant': horz_plant, 'status': status,'inf_canopy':inf_canopy,'spc_latin':spc_latin,'zipcode':zipcode,}})
print(dt_integration)