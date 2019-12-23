from dataset_structure import dataset

def info(dataset, iterator=0):

	keys=list(dataset.keys())

	if(iterator>len(keys)-1):
		return  

	else:	

		if(dataset[keys[iterator]]["average_age"]>30) and (dataset[keys[iterator]]["total_lupa_episodes"]>2):
			print(keys[iterator] + '\t\t   ' + dataset[keys[iterator]]["city"] + ' '*(30-len(dataset[keys[iterator]]["city"])) + str(dataset[keys[iterator]]["total_lupa_episodes"]))
				
		info(dataset, iterator+1)

print("Table info that satisfies conditions : ")
print("\nProvider ID\t\tCity\t\tTotal lupa episodes")
info(dataset)
