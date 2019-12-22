from Tereshenko1.dataset_structure_common import dataset
from Tereshenko1.validator.lib import *


def agency_name_validator(promt):
    re_provider_id=re.compile("^\w+$")
    text = input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text

def male_beneficiaries_validator(promt):
    re_provider_id=re.compile("\s*\d\s*")
    text=input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text

def female_beneficiaries_validator(promt):
    re_provider_id=re.compile("\s*\d\s*")
    text=input(promt)
    while not bool(re_provider_id.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text


def dataset_common_insert(dataset):
    provider_id = provider_id_validator('Enter the provider id ')
    data = {
        "agency_name": agency_name_validator("Enter a agency name"),
        "zip_code": zip_code_validator('Enter zip code'),
        "distinct_beneficiaries_non_lupa": distinct_beneficiaries_non_lupa_validator("Enter a distinct beneficiaries non lupa validator"),
        "average_number_of_total_visits_per_episode_non_lupa": average_number_of_total_visits_per_episode_non_lupa_validator(
            'Enter an average number of total visits per episode non lupa'),
        "male_beneficiaries": male_beneficiaries_validator('Enter a male beneficiaries validator'),
        "female_beneficiaries": female_beneficiaries_validator(
            "Enter a female beneficiaries validator")
    }
    dataset.update({provider_id: data})


dataset_common_insert(dataset)
