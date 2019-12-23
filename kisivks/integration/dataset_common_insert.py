from kisivks.integration.dataset_structure_common import dataset as dataset1
import kisivks.validator.lib as kate_validators
import pyndykivskiytr.validator.lib as taras_validators

key_values = ['provider_id', 'zip_code', 'percent_of_beneficiaries_with_ra_oa',
              'percent_of_beneficiaries_with_stroke', 'city',
              'total_lupa_episodes', 'average_age']


def add_to_dataset(dataset):
    provider_id = 0
    for i in range(4):
        while True:
            value = input(key_values[i] + ' = ')

            if i == 0 and kate_validators.provider_id_validator(value):
                break
            elif i == 1 and kate_validators.zip_code_validator(value):
                break
            elif i == 2 and kate_validators.percent_of_beneficiaries_with_ra_oa_validator(value):
                break
            elif i == 3 and kate_validators.percent_of_beneficiaries_with_stroke_validator(value):
                break
            else:
                print(key_values[i] + ' невірно введений. Введіть повторно\n')

        if i == 0:
            provider_id = value
            dataset[provider_id] = {}
        else:
            dataset[provider_id][key_values[i]] = value

    dataset[provider_id][key_values[4]] = taras_validators.city_validator(taras_validators.pattern_city, key_values[4] + ' = ')
    dataset[provider_id][key_values[5]] = taras_validators.total_lupa_episodes_validator(taras_validators.pattern_total_lupa_episodes, key_values[5] + ' = ')
    dataset[provider_id][key_values[6]] = taras_validators.average_age_validator(taras_validators.pattern_average_age, key_values[6] + ' = ')


add_to_dataset(dataset1)
print(dataset1)
