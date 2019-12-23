import sys
sys.path.append('../../tsakhloev/validator')
from lib import *

sys.path.append('../')
from validator.lib import *

from dataset_structure_common import dataset

def dataset_common_insert(dataset, host_id,room_type, bedrooms, country, cleaning_fee, calendar_updated, extra_people):
	conditions = [room_type_validator(room_type),bedrooms_validator(bedrooms),host_id_validator(host_id),country_validator(country), 
	cleaning_fee_validator(cleaning_fee),calendar_updated_validator(calendar_updated), extra_people_validator(extra_people)]
	if all(conditions):
		dataset.update({
		    host_id:
			   {
			   "room_type":room_type,
	           "bedrooms":bedrooms,
	           "country":country,
	           "cleaning-fee": cleaning_fee,
               "calendar-updated": calendar_updated,
               "extra-people": extra_people
	            }})
		
dataset_common_insert(dataset,"9465817","Private room","1","United States","$35.00","yesterday", "$25.00")

print(dataset)