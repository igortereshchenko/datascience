from RyzhkovaDO.validator.lib import *

#test


objectid = objectid_validator(re_objectid, "Введіть objectid (6 цифр): ")
vert_wall = vert_wall_validator(re_vert_wall, "Введіть vert_wall (Yes/No) : ")
zipcode = zipcode_validator(re_zipcode, "Введіть zipcode (5 цифр): ")
borocode = borocode_validator(re_borocode, "Введіть borocode (Одна цифра з проміжку [1-5]): ")

