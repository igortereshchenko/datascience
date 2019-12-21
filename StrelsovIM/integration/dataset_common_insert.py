import re
from dataset_structure_common import dataset

def insert_line(provider_id, agency_name=None, male_beneficiaries=None, female_beneficiaries=None, state=None, total_episodes_non_lupa=None, total_hha_charge_amount_non_lupa=None, data=dataset):
    data[provider_id] = {
        'agency_name': agency_name,
        'male_beneficiaries': male_beneficiaries,
        'female_beneficiaries': female_beneficiaries,
        'state': state,
        'total_episodes_non_lupa': total_episodes_non_lupa,
        'total_hha_charge_amount_non_lupa': total_hha_charge_amount_non_lupa
    }

def provider_id_validator(id):
    return re.match("^[0-9]{6}$", id)


def agency_name_validator(agency_name):
    return re.match("\s*\D\s*", agency_name)


def male_beneficiaries_validator(male):
    return re.match("\s*\d\s*", male)


def female_beneficiaries_validator(female):
    return re.match("\s*\d\s*", female)


def state_validator(state_name):
    return re.match("^[A-Z]{2}$", state_name)

def total_episodes_non_lupa_validator(total_episodes_non_lupa):
    return re.match("\s*\d\s*", total_episodes_non_lupa)

def total_hha_charge_amount_non_lupa_validator(total_hha_charge_amount_non_lupa):
    return re.match("\s*\d\s*", total_hha_charge_amount_non_lupa)




def validator(valid_function, prompt):
    data = input(prompt)
    if valid_function(data):
        return data
    else:
        return validator(valid_function, prompt)



provider_id_key =validator(provider_id_validator, "id : ")
agency_name_value = validator(agency_name_validator, "agency : ")
male_beneficiaries_value = validator(male_beneficiaries_validator, "male_beneficiaries : ")
female_beneficiaries_value = validator(female_beneficiaries_validator, "female_beneficiaries : ")
state_value = validator(state_validator, "state : ")
total_episodes_non_lupa_value = validator(total_episodes_non_lupa_validator, "total_episodes_non_lupa : ")
total_hha_charge_amount_non_lupa_value = validator(total_hha_charge_amount_non_lupa_validator, "total_hha_charge_amount_non_lupa : ")

insert_line(provider_id_key, agency_name_value, male_beneficiaries_value,female_beneficiaries_value, state_value, total_episodes_non_lupa_value, total_hha_charge_amount_non_lupa_value)

print(dataset)
