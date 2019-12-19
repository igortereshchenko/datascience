from dataset_structure import dataset
from validator.lib import *

def dataset_insert_manual( host_id, cleaning_fee, calendar_updated, extra_people ):

    validators = [ host_id_validator(host_id), cleaning_fee_validator(cleaning_fee), calendar_updated_validator(calendar_updated), extra_people_validator(extra_people) ]

    if all( validators ):

        dataset[int(host_id)] = {
        	
        	'cleaning_fee': cleaning_fee,
        	'calendar_updated': calendar_updated,
        	'extra_people': extra_people

        }

        return True

    return False