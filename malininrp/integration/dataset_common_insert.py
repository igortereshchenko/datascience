from malininrp.validator.lib import *
from SaltykovAn.validator.lib import *
from malininrp.integration.dataset_structure_common import dataset


def input_data():
	data = {}
	validator_keys={'host_name':host_name_validator,
					'street':street_validator,
					'host_response_time':host_response_time_validator,
					'room_type': room_type_validator,
					'price' : price_validator,
					'weekly_price' : weekly_price_validator,
					'beds' : beds_validator}
	keys_numbers = ['host_response_time','price','beds']
	
	for key in validator_keys.keys():
		user_input = input('Enter ur %s '%key)
		
		if validator_keys[key](user_input)[0]:
			data[key]=user_input if key in keys_numbers else float(user_input)
		else:
			data[key]=None
			print(validator_keys[key](user_input)[1])
	
	return data

def data_insert():
	new_id = list(dataset.keys())[-1]+1
	dataset[new_id] = input_data()
	print(dataset[new_id])
	return True


data_insert()