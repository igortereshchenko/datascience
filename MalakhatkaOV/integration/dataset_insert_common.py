from MalakhatkaOV.validator.lib import *
from TernytskaNO.validator.lib import *
from MalakhatkaOV.integration.dataset_structure_common import dataset


def dataset_upd():
    boro = input('boro_code:')
    while not borocode_validator(boro):
        print('Wrong input!')
        boro = input('boro_code:')
    h_plant = input('horz_plant:')
    while not horz_plant_validator(h_plant):
        print('Wrong input!')
        h_plant = input('horz_plant:')
    stat = input('status:')
    while not status_validator(stat):
        print('Wrong input!')
        stat = input('status:')
    wire_o = input('wire_other:')
    while not wire_other_validator(wire_o):
        print('Wrong input!')
        wire_o = input('horz_plant:')
    cen_y = input('cen_year:')
    while not cen_year_validator(cen_y):
        print('Wrong input!')
        cen_y = input('cen_year:')
    wire_p = input('wire_prime')
    while not wire_prime_validator(wire_p):
        print('Wrong input!')
        wire_p = input('wire_prime')
    spc_l = input('spc-latin')
    while not spc_latin_validator(spc_l):
        print('Wrong input!')
        spc_l = input('spc-latin')
    return {
        boro: {
            'horz_plants': h_plant,
            'status': stat,
            'wire_other': wire_o,
            "cen-year": cen_y,
            "wire-prime": wire_o,
            'spc-latin': spc_l
        },
    }


dataset.update(dataset_upd())
