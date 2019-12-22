from torbaso.validator.lib import *
from torbaso.integration.dataset_structure_common import dataset
import re

#Функції з якими відбувається інтеграція(Данилевича)
def extra_people_validator(extra):
    while not re.match('^[+]?\d+[.]?\d{,2}$', extra):
        extra=input("Enter valid extra-price:")
    return extra


def host_id_validator(host_id):
    while not re.match('^[+]?\d+$', host_id):
        host_id=input("Enter valid host-id: ")
    return int(host_id)




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
