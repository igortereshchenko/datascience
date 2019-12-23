from DahovskayaUO.validator.lib import *

if price_validator('20.00'):
    print('Price is correct')
else:
    print('Price is incorrect')
#correct

if code_validator('US'):
    print('Country-code is correct')
else:
    print('Country-code is incorrect')
#correct

if city_validator('newyork'):
    print('City is correct')
else:
    print('City is incorrect')
#incorrect

if street_validator('8th Avenue West, Seattle, WA 98119, United States'):
    print('Street is correct')
else:
    print('Street is incorrect')
#correct