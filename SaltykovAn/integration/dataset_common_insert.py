from SaltykovAn.integration.dataset_structure_common import dataset
from SaltykovAn.validator.lib import *
from torbaso.validator.lib import *

name = name_validator(input("name:"))
country = country_validator(input("country:"))
bed_type =bed_type_validator(input("bed_type:"))
price = price_validator(input("price:"))
room_type = input("room_type:")
while not room_type_validator(room_type):
    room_type = input("Enter valid room_type:")

weekly_price = input("weekly_price:")
while not weekly_price_validator(weekly_price):
    weekly_price = input("Enter valid weekly_price:")

beds = input("beds:")
while not beds_validator(beds):
    beds = input("Enter valid number of beds:")


def add_el(data_set,country,bed_type,price,room_type,weekly_price,beds):
    data_set.update ({
        name: {
             'country':country,
             'bed-type':bed_type,
             'price':price,
             'room_type':room_type,
             'weekly_price': weekly_price,
             'beds': beds
        }
    })
    return data_set

add_el(dataset,country,bed_type,price,room_type,weekly_price,beds)

print(dataset)



