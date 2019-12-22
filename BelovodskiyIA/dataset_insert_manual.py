from BelovodskiyIA.dataset_structure import data_structure

new_id = list(data_structure.keys())[-1]+1

data_structure[new_id] = {
					'host_name': 'Ivan',
					'host_verifications' : ['email', 'phone'],
					'state' : 'WA',
					'market' : 'Seattle'
					}
print(data_structure)
