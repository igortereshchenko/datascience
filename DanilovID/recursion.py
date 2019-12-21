from dataset_structure import dataset

def recursion(dataset, n = None):
	
    if n == None: 
    	n = len(dataset) - 1

    elif n == -1: 
    	return None

    keys_of_dataset = list(dataset.keys())

    amount_of_bedrooms = int(dataset[keys_of_dataset[n]]['bedrooms']) 
    type_of_rooms = dataset[keys_of_dataset[n]]['room_type']
    host_id = [keys_of_dataset[n]]
    country = dataset[keys_of_dataset[n]]['country']


    if amount_of_bedrooms>= 2 or type_of_rooms.find('Private room') != -1:
        print('#room_type: ',type_of_rooms, '#host_id:',host_id, '#country:', country)

    recursion(dataset, n-1)

recursion(dataset)
