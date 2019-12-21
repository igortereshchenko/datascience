import pycountry


def country_validator(country):
    countries = (i.name for i in list(pycountry.countries))
    if country not in countries:
        return False
    else:
        return True



def number_of_reviews_validator(number_of_reviews):
    if isinstance(number_of_reviews, int) and number_of_reviews >= 0:
        return True
    else:
        return False


def review_scores_value_validator(review_scores_value):
    if isinstance(review_scores_value, int) and 0 <= review_scores_value <= 100:
        return True
    else:
        return False

def host_id_validator(host_id):
    if isinstance(host_id, int) and 0 <= host_id < 1000000:
        return True
    else:
        return False


import re


def price_validator(price):
    if re.match('^\d+\.{0,1}\d*$', str(price)):
        return True
    return False

def code_validator(country_code):
    if re.match('^[A-Z]{2}$', str(country_code)):
        return True
    return False

def city_validator(city):
    if re.match('^([A-Z](?:[a-z]+[- ]*))+$', str(city)):
        return True
    return False

def street_validator(street):
    if re.match('^(?:[\w./,:; ])+$', str(street)):
        return True
    return False

from dataset_structure_common import dataset

def dataset_common_insert(dataset):

    number_of_reviews = input('Enter number of reviews: ')
    while not number_of_reviews_validator(number_of_reviews):
        number_of_reviews = input('Incorrect! Enter valid number of reviewes: ')

    review_scores_value = input('Enter review_scores_value: ')
    while not  review_scores_value_validator(review_scores_value):
        review_scores_value = input('Incorrect! Enter valid review scores value: ')

    country = input('Enter country: ')
    while not country_validator(country):
        country = input('Incorrect! Enter valid country: ')

    street = input('Enter street: ')
    while not street_validator(street):
        street = input('Incorrect! Enter valid street: ')

    country_code = input('Enter country code: ')
    while not code_validator(country_code):
        country_code = input('Incorrect! Enter valid country code: ')

    price = input('Enter price: ')
    while not price_validator(price):
        price = input('Incorrect! Enter valid price: ')

    city = input('Enter city: ')
    while not city_validator(city):
        city = input('Incorrect! Enter valid city: ')

    host_id = input('Enter host ID: ')
    while not host_id_validator(host_id):
        host_id = input('Incorrect! Enter valid host ID: ')

    new_data = {
        host_id:
            {
                'number_of_reviews': number_of_reviews,
                'review_scores_value': review_scores_value,
                'country': country,
                'street': street,
                'country_code': country_code,
                'price': price,
                'city': city
            }
    }

    dataset.update(new_data)

dataset_common_insert(dataset)