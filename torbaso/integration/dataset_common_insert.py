from torbaso.validator.lib import *
from torbaso.dataset_structure import dataset
from danylevichoo.validator.lib import extra_people_validator,host_id_validator
import re


country =input('Enter country name')
name = input('Enter name of accomodation')
price = float(input('Enter price of 1 night in this offer'))
bed_type =input('Enter bed_type')
host_id = input('Enter host-id')
extra_people = input('Enter extra-people')




newhotel = {
    4:{
        'name':name_validator(name),
        'country':country_validator(country),
        'bed-type':bed_type_validator(bed_type),
        'price':price_validator(price),
        'host-id':host_id_validator(host_id),
        'extra-people':extra_people_validator(extra_people)
        
    }
}

dataset.update(newhotel)
