from chernyshaa.validator.lib import *
from ZaytsevED.validator.lib import *
from chernyshaa.integration.dataset_structure_common import dataset

provider_id = provider_id_validator(input("Введіть будь ласка ідентифікаційний номер: "))
agency_name = agency_name_validator(input('Введіть будь ласка назву агенції: '))
total_lupa_edisodes = total_lupa_edisodes_validator(input('Введіть будь ласка залну суму платежів : '))
avarage_age = avarage_age_validator(input('Введіть будь ласка середній рік: '))
state = state_validator(input('Введіть будь ласка стан, в якому знаходиться агенство: '))
white_beneficiaries = white_beneficiaries_validator(input('Введіть будь ласка кількість не латиномовних користувачів: '))
black_beneficiaries = black_beneficiaries_validator(input('Введіть будь ласка кількість неіспаномовних користувачів : '))

dataset[provider_id] = {
    'agency_name': agency_name,
    'total_lupa_edisodes':total_lupa_edisodes,
    'avarage_age':avarage_age,
    'state' : state,
    'white_beneficiaries' : white_beneficiaries,
    'black_beneficiaries' : black_beneficiaries
}

print(dataset)
