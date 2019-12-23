from RyzhkovaDO.validator.lib import *
from RyzhkovaDO.integration.validator_lib_NoskovIlyas import *

dataset = {
           698612:{
               2005:{
                'vert_wall': "No"
                ,'zipcode': 10471
                ,'borocode': 2
                ,'zip_city': "Bronx"
                ,'horz_grate': "no"
                ,'spc_common': "London Planetree"
                     }
                  }
           ,860288:{
                2006:{
                'vert_wall': "No"
                ,'zipcode': 11432
                ,'borocode': 4
                ,'zip_city': "Jamaica"
                ,'horz_grate': "no"
                ,'spc_common': "Elm, oter"
                     }
                   }
           ,641807:{
                2006:{
                'vert_wall': "No"
                ,'zipcode': 10007
                ,'borocode': 1
                ,'zip_city': "New York"
                ,'horz_grate': "no"
                ,'spc_common': "Honeylocust"
                     }
                   }
           }


objectid = objectid_validator(re_objectid, "Введіть objectid (6 цифр): ")
vert_wall = vert_wall_validator(re_vert_wall, "Введіть vert_wall (Yes/No) : ")
zipcode = zipcode_validator(re_zipcode, "Введіть zipcode (5 цифр): ")
borocode = borocode_validator(re_borocode, "Введіть borocode (Одна цифра з проміжку [1-5]): ")
zip_city = key_valid("Введіть назву міста: ")
horz_grate = horzgr_valid("Чи є решітки з дерева (yes/no)?: ")
spc_common = spc_valid("Введіть загальна назву виду: ")
cen_year = year_valid("Введіть рік у якому було інвентаризовано дерево (4 цифр): ")

dataset.update({objectid: {cen_year: {'vert_wall': vert_wall, 'zipcode': zipcode, 'borocode': borocode,
                               'zip_city': zip_city, 'horz_grate': horz_grate, 'spc_common': spc_common, 'cen_year': cen_year}}})


print(dataset)