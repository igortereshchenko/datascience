from DahnovskaUO.validator import *
from bespalovad.validator import *
from dataset_structure_common import dataset

def dataset_common_insert(dataset):

    street = input('Enter street: ')
    while not street_validator(street):
        street = input('Incorrect! Enter valid street: ')

    host_url = input('Enter Host Url: ')
    while not host_url_validator(host_url):
        host_url = input('Incorrect! Enter valid Host Url:' )

    host_since = input('Enter Host Since: ')
    while not host_since_validator(host_since):
        host_since = input('Incorrect! Enter valid Host Since:' )

    zipcode = input('Enter Zipcode: ')
    while not zipcode_validator(zipcode):
        zipcode = input('Incorrect! Enter valid Zipcode: ')

    country = input('Enter country: ')
    while not country_validator(country):
        country = input('Incorrect! Enter valid country: ')

    country_code = input('Enter country code: ')
    while not code_validator(country_code):
        country_code = input('Incorrect! Enter valid country code:' )

    city = input('Enter city: ')
    while not city_validator(city):
        city = input('Incorrect! Enter valid city: ')

    price = input('Enter price: ')
    while not price_validator(price):
        price = input('Incorrect! Enter valid price: ')

    new_data = {
        street:
            {
                'host_url': host_url,
                'host_since': host_since,
                'zipcode': zipcode,
                'country': country,
                'country_code': country_code,
                'city': city,
                'price': price
            }
    }

    dataset.update(new_data)

dataset_common_insert(dataset)
