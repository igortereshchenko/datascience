from dovgaleo.integration.dataset_structure_common import dataset
from dovgaleo.integration import validator


key_validators = {
        'provider_id': validator.provider_id_validator,
        'city': validator.city_validator,
        'zip_code': validator.zip_code_validator,
        'total_episodes_non_lupa': validator.total_episodes_non_lupa_validator,
        'percent_of_beneficiaries_with_ra_oa': validator.percent_of_beneficiaries_with_ra_oa_validator,
        'percent_of_beneficiaries_with_stroke': validator.percent_of_beneficiaries_with_stroke_validator
}


def insert_common_data(dataset):
    if not isinstance(dataset, dict):
        print('Your dataset is not valid')
        return -1

    provider_id, value = 0, 0
    for key, validator in key_validators.items():
        data_is_valid = False
        while not data_is_valid:
            value = input(f'{key} = ')
            data_is_valid = validator(value)

        if provider_id == 0:
            provider_id = value
            dataset[value] = {}
        else:
            dataset[provider_id][key] = value


insert_common_data(dataset)

print('\ndataset:')
for key, value in dataset.items():
    print('id', key, value)
