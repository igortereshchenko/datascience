from malininrp.dataset_structure import dataset


dict_keys = list(dataset.keys())

def show_data(data_structure,keys):

	if not len(keys):
		return False
	else:
		if data_structure[keys[0]]['host_response_time']>10 and data_structure[keys[0]]['host_response_time']<50:
			for k in data_structure[keys[0]].keys():
				if k != 'host_response_time':
					print(data_structure[keys[0]][k])
			print(keys[0])
			print('\n')
		return show_data(data_structure,keys[1:])

show_data(dataset,dict_keys)
