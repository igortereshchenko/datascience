

from tansa25.validator.lib import *
from tansa25.integration.dataset_structure_common import dataset


import re


def room_type_validator(type):
    if re.match(r'[A-Z][a-z]*\s+(room|home/apt|apt/home)', type):
        return True
    else:
        return False


def bedrooms_validator(bedrooms):
    if re.match(r'^\d+$', bedrooms):
        return True
    else:
        return False


def host_id_validator(id):
    if re.match(r'^\d+$', id):
        return True
    else:
        return False


def country_validator(country):
    if re.match(r'^([A-Z]([a-z]*\s?))*$', country):
        return True
    else:
        return False


def price_validator(price):
    if re.match(r'^\$\d+.?\d*$', price):
        return True
    else:
        return False


def minimum_nights_validator(minimum):
    if re.match(r'^\d+$', minimum):
        return True
    else:
        return False


def weekly_price_validator(weekly_price):
    if re.match(r'^\$\d+.?\d*$', weekly_price):
        return True
    else:
        return False


dataset = {
    956883:
        {
            "price": "$85",
            "minimum_nights": "1",
            "weekly_price": "$600 ",
            "coutry": "United States",
            "room_type": "Entire home/apt",
            "bedrooms": "1"
        },

    5177328:
        {

            "price": "$150",
            "minimum_nights": "2",
            "weekly_price": "$1000 ",
            "coutry": "United States",
            "room_type": "Entire home/apt",
            "bedrooms": "1"

        },

    16708587:

        {
            "price": "$975",
            "minimum_nights": "4",
            "weekly_price": "$2000",
            "coutry": "United States",
            "room_type": "Entire home/apt",
            "bedrooms": "5"
        }
}


def dataset_common_insert(dataset, host_id, room_type, bedrooms, country, price, minimum_nights, weekly_price):
    conditions = [room_type_validator(room_type), bedrooms_validator(bedrooms), host_id_validator(host_id),
                  country_validator(country),
                  price_validator(price), minimum_nights_validator(minimum_nights),
                  weekly_price_validator(weekly_price)]
    if all(conditions):
        dataset.update({
            host_id:
                {
                    "room_type": room_type,
                    "bedrooms": bedrooms,
                    "country": country,
                    "price": price,
                    "minimum_nights": minimum_nights,
                    "weekly_price": weekly_price
                }})


dataset_common_insert (dataset, "53050", "Entire home/apt", "1", "United States", "$129.00", "5", "$903.00")

print(dataset)