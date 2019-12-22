import re
from yarovoyde.dataset_structure_common import dataset
from yarovoyde.validator.lib import provider_id_validator, city_validator,percent_of_beneficiaries_with_cancer_validator,percent_of_beneficiaries_with_diabetes_validator

def insert_line(provider_id, agency_name=None, male_beneficiaries=None, city=None, female_beneficiaries=None, percent_of_beneficiaries_with_cancer=None, percent_of_beneficiaries_with_diabetes=None, data=dataset):
    data[provider_id] = {
        'agency_name': agency_name,
        'male_beneficiaries': male_beneficiaries,
        'city': city,
        'female_beneficiaries': female_beneficiaries,
        'percent_of_beneficiaries_with_cancer': percent_of_beneficiaries_with_cancer,
        'percent_of_beneficiaries_with_diabetes': percent_of_beneficiaries_with_diabetes
    }

def main(valid_function, prompt):
    data = input(prompt)
    if valid_function(data):
        return data
    else:
        return main(valid_function, prompt)

def agency_name_validator(promt):
    re_provider_id=re.compile("^\w+$")
    text=input(promt)
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

id_key = main(provider_id_validator, "id : ")
agency_name_value = main(agency_name_validator, "agency : ")
male_beneficiaries_value = main(male_beneficiaries_validator, "male_beneficiaries : ")
city_value = main(city_validator, "city : ")
female_beneficiaries_value = main(female_beneficiaries_validator, "female_beneficiaries : ")
percent_of_beneficiaries_with_cancer_value = main(percent_of_beneficiaries_with_cancer_validator, "percent_cancer : ")
percent_of_beneficiaries_with_diabetes_value = main(percent_of_beneficiaries_with_diabetes_validator, "percent_diabetes : ")

insert_line(id_key, agency_name_value, male_beneficiaries_value, city_value, female_beneficiaries_value, percent_of_beneficiaries_with_cancer_value, percent_of_beneficiaries_with_diabetes_value)

print(dataset)