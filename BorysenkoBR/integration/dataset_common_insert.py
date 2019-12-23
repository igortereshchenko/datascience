from dataset_structure_common import dataset
from validator.lib import *


def zip_code_validator(promt):
    re_zip_code = re.compile("^\d{5}$")
    text = input(promt)
    while not bool(re_zip_code.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text


def average_age_validator(promt):
    re_average_age = re.compile("^\d{2,3}$")
    text = input(promt)
    while not bool(re_average_age.match(text)):
        text = input("Invalid data, try entering the provider id again")
    return text


def percent_of_beneficiaries_with_stroke_validator(promt):
    re_stroke = re.compile("^\d{1,3}$")
    text = input(promt)
    while not bool(re_stroke.match(text)) or int(text) > 100:
        text = input("Invalid data, try entering the percent of beneficiaries with osteoporosis again")
    return text


def dataset_common_insert(dataset):
    provider_id = provider_id_validator('Enter the provider id ')
    data = {
        "city": city_validator("Enter a city name"),
        "zip_code": zip_code_validator('Enter zip code'),
        "average_age": average_age_validator("Enter an avarage age of beneficiaries"),
        "percent_of_beneficiaries_with_osteoporosis": percent_of_beneficiaries_with_osteoporosis_validator(
            'Enter the percent of beneficiaries with osteoporosis'),
        "percent_of_beneficiaries_with_schizophrenia": percent_of_beneficiaries_with_schizophrenia_validator(
            'Enter the percent of beneficiaries with schizophrenia'),
        "percent_of_beneficiaries_with_stroke": percent_of_beneficiaries_with_stroke_validator(
            "Enter the percent of beneficiaries with stroke")
    }
    dataset.update({provider_id: data})


dataset_common_insert(dataset)
