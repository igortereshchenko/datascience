from Matvienko.validator.lib import *

print(cen_year_validator("2015"))
print(cen_year_validator("20006"))
print(horz_plant_validator("No"))
print(horz_plant_validator("qwer"))
print(vert_wall_validator("Yes"))
print(vert_wall_validator("yes"))
print(sidw_raise_validator("123665"))
print(sidw_raise_validator("no"))
