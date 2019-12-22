import importlib
from torbaso.validator.lib import *
country =input('Enter country name')
name = input('Enter name of accomodation')
price = float(input('Enter price of 1 night in this offer'))
bed_type =input('Enter bed_type')

print(country_validator(country))
print(name_validator(name))
print(price_validator(price))
print(bed_type_validator(bed_type))