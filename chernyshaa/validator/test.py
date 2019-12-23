from chernyshaa.validator.lib import provider_id_validator, agency_name_validator,total_lupa_edisodes_validator,avarage_age_validator
from chernyshaa.dataset_structure import dataset

provider_id = provider_id_validator(input("Введіть будь ласка ідентифікаційний номер: "))
agency_name = agency_name_validator(input('Введіть будь ласка назву агенції: '))
total_lupa_edisodes = total_lupa_edisodes_validator(input('Введіть будь ласка залну суму платежів : '))
avarage_age = avarage_age_validator(input('Введіть будь ласка середній рік: '))

dataset[provider_id] = {
    'agency_name': agency_name,
    'total_lupa_edisodes':total_lupa_edisodes,
    'avarage_age':avarage_age
}

print(dataset)
