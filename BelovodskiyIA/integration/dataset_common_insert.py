from malininrp.validator.lib import *
from BelovodskiyIA.validator.lib import *
from BelovodskiyIA.integration.dataset_structure_common import data_structure


def input_data():
	data = {}
	validator_keys={'host_name':host_name_validator,
					'host_verifications':host_verifications_validator,
					'state':state_validator,
					'market':market_validator,
					'street':street_validator,
					'host_response_time':host_response_time_validator}
	for key in validator_keys.keys():
		user_input = input('Enter ur %s '%key)
		
		if validator_keys[key](user_input)[0]:
			data[key]=user_input if key!='host_response_time' else float(user_input)
		else:
			data[key]=None
			print(validator_keys[key](user_input)[1])
	
	return data

def data_insert():
	new_id = list(data_structure.keys())[-1]+1
	data_structure[new_id] = input_data()		
	print(data_structure[new_id])
	return True


data_insert()
