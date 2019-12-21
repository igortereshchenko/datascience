from PankeyevaSD.dataset_structure import dataset
from PankeyevaSD.validator.lib import id_validator, zip_code_validator, percent_of_beneficiaries_with_copd_validator, percent_of_beneficiaries_with_hypertension_validator
from BorysenkoBR.validator.lib import city_validator, percent_of_beneficiaries_with_osteoporosis_validator, percent_of_beneficiaries_with_schizophrenia_validator

def insert_line(provider_id, zip_code=None, percent_of_beneficiaries_with_copd = None,percent_of_beneficiaries_with_hypertension = None, city=None, percent_of_benefciaries_with_osteoporosis =None,percent_of_beneficiaries_with_schizophrenia =None, data=dataset):
    data[provider_id] = {
        'zip_code': zip_code,
        'percent_of_beneficiaries_with_copd': percent_of_beneficiaries_with_copd,
        'percent_of_beneficiaries_with_hypertension': percent_of_beneficiaries_with_hypertension,
        'city': city,
        'percent_of_benefciaries_with_osteoporosis': percent_of_benefciaries_with_osteoporosis,
        'percent_of_beneficiaries_with_schizophrenia': percent_of_beneficiaries_with_schizophrenia
    }


def main(validator_function, message):
    data = input(message)
    if validator_function(data):
        return data
    else:
        return main(validator_function, message)


id_key = main(id_validator, "id : ")
zip_code_value = main(zip_code_validator, "zip : ")
percent_of_beneficiaries_with_copd_value = main(percent_of_beneficiaries_with_copd_validator, "percent_copd : ")
percent_of_beneficiaries_with_hypertension_value = main(percent_of_beneficiaries_with_hypertension_validator, "percent_hypertension : ")
city_value = city_validator("city : ")
percent_of_beneficiaries_with_osteoporosis_value = percent_of_beneficiaries_with_osteoporosis_validator("percent_osteoporosis : ")
percent_of_beneficiaries_with_schizophrenia_value = percent_of_beneficiaries_with_schizophrenia_validator("percent_schizophrenia : ")

insert_line(id_key,
            zip_code_value,
            percent_of_beneficiaries_with_copd_value,
            percent_of_beneficiaries_with_hypertension_value,
            city_value,
            percent_of_beneficiaries_with_osteoporosis_value,
            percent_of_beneficiaries_with_schizophrenia_value)

print(dataset)


