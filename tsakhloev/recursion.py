from dataset_structure import dataset

def recursion( dataset ):

	if not dataset:
		return

	key = list(dataset.keys())[0]
	data = dataset[key]

	extraPeople = data['extra-people']
	cleaningFee = data['cleaning-fee']

	if ( extraPeople != None and float(extraPeople[1:]) > 100 ) or ( cleaningFee != None and float(cleaningFee[1:]) ) > 30:
		print( f'host-id: {key}, extra-people: {extraPeople}, cleaning-fee: {cleaningFee}' )

	dataset_copy = dataset.copy()
	del dataset_copy[key]

	recursion( dataset_copy )