from bondarilya.integration.dataset_structure_common import dataset
from bondarilya.validator.lib import *


def avarage_age_vr():
    return


def male_beneficiares_vr():
    return


def female_beneficaries_vr():
    return


def dataset_input():
    id = provider_id_vr()
    state = state_vr()
    unknown = other_unknown_beneficiaries_vr()
    alzheimers = percent_of_beneficiaries_with_alzheimers_vr()
    age = avarage_age_vr()
    male = male_beneficiares_vr()
    female = female_beneficaries_vr()
    add_data = {
        "state": state,
        "other_unknown_beneficiaries": unknown,
        "percent_of_beneficiaries_with_alzheimers": alzheimers,
        'avarage_age': age,
        'male_beneficiares': male,
        'female_beneficaries': female
    }
    dataset.update({id: add_data})


dataset_input()
