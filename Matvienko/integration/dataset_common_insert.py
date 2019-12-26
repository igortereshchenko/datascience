from Matvienko.integration.dataset_structure_common import dataset
from Matvienko.validator.lib import *
from usatovsv.validator.lib import *

def dataset_common_insert(dataset):
    cen_year=input("enter cen_year: ")
    while not cen_year_validator(cen_year):
        cen_year = input("enter cen_year: ")

    horz_plant=input("enter horz_plant: ")
    while not horz_plant_validator(horz_plant):
         horz_plant=input("enter horz_plant: ")

    vert_wall=input("enter vert_wall: ")
    while not vert_wall_validator(vert_wall):
         vert_wall=input("enter vert_wall: ")

    sidw_raise=input("enter sidw_raise: ")
    while not sidw_raise_validator(sidw_raise):
         sidw_raise=input("enter sidw_raise: ")

    cb_num=input("enter cb_num: ")
    while not cb_num_validator(cb_num):
         cb_num=input("enter cb_num: ")

    wire_2nd=input("enter wire_2nd: ")
    while not wire_2nd_validator(wire_2nd):
         wire_2nd=input("enter wire_2nd: ")

    spc_latin=input("enter spc-latin: ")
    while not spc_latin_validator(spc_latin):
         spc_latin=input("enter spc-latin: ")

    zipcode=input("enter zipcode: ")
    while not zipcode_validator(zipcode):
         zipcode=input("enter zipcode: ")



    input_data = {zipcode: {
        "cen_year": cen_year,
        "horz_plant": horz_plant,
        "vert_wall": vert_wall,
        "sidw_raise": sidw_raise,
        "cb_num": cb_num,
        "wire_2nd": wire_2nd,
        "spc-latin": spc_latin
                             }
        }
    return input_data
dataset.update(dataset_common_insert(dataset))

print(dataset)
