from dataset_structure import dataset

def recursion( dataset, keys = None ):

	if keys == None:
		keys = list(dataset.keys())
	elif not keys:
		return

	data = dataset[keys[0]]

	extraPeople = data['extra-people']
	cleaningFee = data['cleaning-fee']

	if ( extraPeople != None and float(extraPeople[1:]) > 100 ) or ( cleaningFee != None and float(cleaningFee[1:]) ) > 30:
		print( f'host-id: {keys[0]}, extra-people: {extraPeople}, cleaning-fee: {cleaningFee}' )

	del keys[0]

	recursion( dataset, keys )