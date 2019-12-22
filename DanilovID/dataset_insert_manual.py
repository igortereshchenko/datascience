from dataset_structure import dataset
from validator.lib import *
def dataset_insert_manual(dataset, host_id,room_type, bedrooms, country):
	conditions = [room_type_validator(room_type),bedrooms_validator(bedrooms),host_id_validator(host_id),country_validator(country)]
	if all(conditions):
		dataset.update({
		    host_id:
			   {
			   "room_type":room_type,
	           "bedrooms":bedrooms,
	           "country":country
	            }})


dataset_insert_manual(dataset,"243056","Shared room","1","United States")

print(dataset)
