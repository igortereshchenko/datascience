from ZaytsevED.validator.lib import *
from ZaytsevED.integration.dataset_structure_common import dataset
from holenyshchenkosd.validator.lib import *


def dataset_insert(dataset, prov_id, state, wh_benef, bl_benef, perc_of_benef_with_cancer, perc_of_benef_with_depres):
    dataset[prov_id] = {
        'state': state,
        'white_beneficiaries': wh_benef,
        'black_beneficiaries': bl_benef,
        'percent_of_beneficiaries_with_cancer': perc_of_benef_with_cancer,
        'percent_of_beneficiaries_with_depression': perc_of_benef_with_depres
    }


provide_id = provide_id_validator(input('Input the 6-digit identification number for the home health agency: '))
state = state_validator(input('Input state where agency is located: '))
white_beneficiaries = white_beneficiaries_validator(input('Input number of non-Hispanic white beneficiaries: '))
black_beneficiaries = black_beneficiaries_validator(input('Input number of non-Hispanic black or African American beneficiaries: '))
percent_of_beneficiaries_with_cancer = percent_of_beneficiaries_with_cancer_validator(input("Input percent of beneficiaries meeting the CCW chronic condition algorithms for cancer: "))
percent_of_beneficiaries_with_depression = percent_of_beneficiaries_with_depression_validator(input("Input percent of beneficiaries meeting the CCW chronic condition algorithm for depression: "))

dataset_insert(dataset, provide_id, state, white_beneficiaries, black_beneficiaries, percent_of_beneficiaries_with_cancer, percent_of_beneficiaries_with_depression)
print(dataset)
