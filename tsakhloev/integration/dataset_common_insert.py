import sys
sys.path.append('../../shchehelskyiho/validator')
from lib import *

sys.path.append('../')
from validator.lib import *

from dataset_structure_common import dataset

def dataset_insert_manual( dataset, ID, data ):

    id_validator = host_id_validator

    validators = {

        'cleaning_fee': cleaning_fee_validator,
        'extra_people': extra_people_validator,
        'space': space_validator,
        'street': street_validator,
        'zipcode': zipcode_validator

    }

    validators_result = [ id_validator( ID ) ]
    validators_result += [ validators[tag]( data[tag] ) for tag in data.keys() ]

    if all( validators_result ):

        dataset[int(ID)] = data

        none_tags = set( validators.keys() ) - set(data.keys())
        for tag in none_tags:
            dataset[int(ID)][tag] = None

        return True

    return False

#dataset_insert_manual( dataset, '123', { 'cleaning_fee': '$1.00' } )
#print( dataset )