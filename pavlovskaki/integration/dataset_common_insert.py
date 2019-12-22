from pavlovskaki.integration.dataset_structure_common import dataset
from pavlovskaki.validator.lib import id_validator, agency_name_validator, street_adress_validator, city_validator
from PankeyevaSD.validator.lib import zip_code_validator, percent_of_beneficiaries_with_copd_validator, percent_of_beneficiaries_with_hypertension_validator


def insert_line(id_value, agency_name=None, street_adress=None, city=None, zip_code=None, percent_copd=None, percent_hypertension=None, data=dataset):
    data[id_value] = {
        'agency_name': agency_name,
        'street_adress': street_adress,
        'city': city,
        'zip_code': zip_code,
        'percent_of_beneficiaries_with_copd': percent_copd,
        'percent_of_beneficiaries_with_hypertension': percent_hypertension
    }


def main(valid_function, prompt):
    data = input(prompt)
    if valid_function(data):
        return data
    else:
        return main(valid_function, prompt)


id_key = main(id_validator, "id : ")
agency_name_value = main(agency_name_validator, "agency : ")
street_adress_value = main(street_adress_validator, "street : ")
city_value = main(city_validator, "city : ")
zip_code_value = main(zip_code_validator, "zip : ")
percent_of_beneficiaries_with_copd_value = main(percent_of_beneficiaries_with_copd_validator, "percent_copd : ")
percent_of_beneficiaries_with_hypertension_value = main(percent_of_beneficiaries_with_hypertension_validator, "percent_hypertension : ")

insert_line(id_key, agency_name_value, street_adress_value, city_value, zip_code_value, percent_of_beneficiaries_with_copd_value, percent_of_beneficiaries_with_hypertension_value)

print(dataset)
