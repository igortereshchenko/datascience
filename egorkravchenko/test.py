from validator.lib import zip_code_validator, provider_id_validator, distinct_beneficiaries_non_lupa_validator, average_number_of_total_visits_per_episode_non_lupa_validator
from dataset_structure import dataset
provider_id = provider_id_validator(input("Enter provider ID : "))

zip_code = zip_code_validator(input("Enter the zip code name : "))

distinct_beneficiaries_non_lupa = distinct_beneficiaries_non_lupa_validator(input("Enter the number of beneficiaries non lupa: "))

average_number_of_total_visits_per_episode_non_lupa = average_number_of_total_visits_per_episode_non_lupa_validator(input("EEnter the number of episode non lupa: "))

dataset[provider_id] = {
    'zip_code': zip_code,
    'distinct_beneficiaries_non_lupa': distinct_beneficiaries_non_lupa,
    'average_number_of_total_visits_per_episode_non_lupa': average_number_of_total_visits_per_episode_non_lupa
}

print(dataset)