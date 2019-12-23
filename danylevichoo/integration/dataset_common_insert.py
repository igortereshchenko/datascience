from torbaso.validator.lib import country_validator
from torbaso.validator.lib import name_validator
from dataset_structure_common import data_set
from validator.lib import *


def insrt(data_set):
    data_set[len(data_set)+1] = {
        "country":country_validator(input("Enter country:")),
        "name":name_validator(input("Enter name: ")),
        "host-id": host_validator("Enter host-id: "),
        "bed-type": bed_type_validator("Enter type of bed: "),
        "price": price_validator("Enter price: "),
        "extra-people": extra_people_validator("Enter extra-price: ")
    }

print(data_set)