from datascience.pobiedimskasi.validator.lib import *
from datascience.pyndykivskiytr.validator.lib import *  

from dataset_structure_common import dataset

def insert(dataset):

	provider_id=provider_id_validator(pattern_provider_id, "Enter provider ID : ")

	info=dict()

	city=city_validator(pattern_city, "Enter the city name : ")
	info["city"]=city

	total_lupa_episodes=total_lupa_episodes_validator(pattern_total_lupa_episodes, "Enter the number of total lupa episodes : ")
	info["total_lupa_episodes"]=total_lupa_episodes

	average_age=average_age_validator(pattern_average_age, 	"Enter the average age : ")
	info["average_age"]=average_age

	state=state_validator()
	info["state"]=state

	percent_of_beneficiaries_with_depression=percent_of_beneficiaries_with_depression_validator()
	info["percent_of_beneficiaries_with_depression"]=percent_of_beneficiaries_with_depression

	percent_of_beneficiaries_with_hyperlipidemia=percent_of_beneficiaries_with_hyperlipidemia_validator()
	info["percent_of_beneficiaries_with_hyperlipidemia"]=percent_of_beneficiaries_with_hyperlipidemia

	dataset[provider_id]=info
	
	return dataset

cont=""
while(cont==""):
	dataset=insert(dataset)
	cont=input("Press Enter to continue, other key to leave : ")

