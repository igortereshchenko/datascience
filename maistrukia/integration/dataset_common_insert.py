import maistrukia.integration.dataset_structure_common as mds
import Ivanova_es.validator.lib as elib
import maistrukia.validator.lib as mlib

#cen_year, whire_htap, horz_plant, inf-shoes, inf-canopy, cb_num, zip_city, spc_latin

def spc_latin_input(description_str=""):
    temp_str = input(description_str)
    while not elib.latin_name_validator(temp_str):
        temp_str = input()
    return temp_str

def cen_year_input(description_str=""):
    temp_str = input(description_str)
    while not elib.cen_year_validator(temp_str):
        temp_str = input()
    return int(temp_str)

def horz_plant_input(description_str=""):
    temp_str = input(description_str)
    while not elib.horz_plant_validator(temp_str):
        temp_str = input()
    return bool(temp_str)

def whire_htap_input(description_str=""):
    temp_str = input(description_str)
    while not elib.whire_htap_validator(temp_str):
        temp_str = input()
    return bool(temp_str)

def inf_canopy_input(description_str=""):
    temp_str = input(description_str)
    while not mlib.inf_canopy_validator(temp_str):
        temp_str = input()
    return temp_str

def inf_shoes_input(description_str=""):
    temp_str = input(description_str)
    while not mlib.inf_shoes_validator(temp_str):
        temp_str = input()
    return temp_str

def zip_city_input(description_str=""):
    temp_str = input(description_str)
    while not mlib.zip_city_validator(temp_str):
        temp_str = input()
    return temp_str

def cb_num_input(description_str=""):
    temp_str = input(description_str)
    while not mlib.cb_num_validator(temp_str):
        temp_str = input()
    return int(temp_str)

def add(dataset, spc_latin, cb_num, inf_c, inf_s, zip_city, cen_year, whire_htap, horz_plant):
    print(dataset)
    if spc_latin not in dataset.keys():
        dataset.update(dict({spc_latin: {}}))
    if zip_city not in dataset[spc_latin].keys():
        dataset[spc_latin].update(dict({zip_city: {}}))
    if cb_num not in dataset[spc_latin][zip_city].keys():
        dataset[spc_latin][zip_city].update(dict({cb_num: {}}))
    dataset[spc_latin][zip_city].update({
        cb_num: {
            "inf-canopy": inf_c
            , "inf-shoes": inf_s
            , "cen_year": cen_year
            , 'whire_htap': whire_htap
            , 'horz_plant': horz_plant
        },
    })

sps_latin = spc_latin_input("Введіть назву дерева: ")
cb_num = cb_num_input("Введіть номер громади: ")
inf_canopy = inf_canopy_input("Введіть наявність навісу: ")
inf_shoes = inf_shoes_input("Введіть наявність слідів: ")
zip_city = zip_city_input("Введіть назву міста: ")
cen_year = cen_year_input("Введіть рік інвентаризації дерева: ")
whire_htap = whire_htap_input("Введіть наявність дротів: ")
horz_plant = horz_plant_input("Введіть наявність самого дерева: ")

add(mds.dataset, sps_latin, cb_num, inf_canopy, inf_shoes, zip_city, cen_year, whire_htap, horz_plant)
print(mds.dataset)