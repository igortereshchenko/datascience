from dataset_structure_common import dataset
from validator.lib import *

def state_validator(promt):
    re_state = re.compile("^[A-W]{2}$")
    value = input(promt)
    while not re_state.match(value) or len(value) > 2:
        value = input("Incorrect input, try again:\n")
    return value
    
    
def asian_pacific_islander_beneficiaries_validator(promt):
    re_asian_pacific_islander_beneficiaries = re.compile("^\d")
    value = input(promt)
    while not re_asian_pacific_islander_beneficiaries.match(value):
        value = input("Incorrect input, try again:\n")
    return value
    
    
def hispanic_beneficiaries_validator(promt):
    re_hispanic_beneficiaries = re.compile("^\d")
    value = input(promt)
    while not re_hispanic_beneficiaries.match(value):
        value = input("Incorrect input, try again:\n")
    return value
    

def dataset_common_insert(unique_number_of_patient, dataset):
    dataset[unique_number_of_patient] = \
        {"agency_name": agency_name_validator("MAXIM INC"),
         "average_hcc_score": average_hcc_score_validator("3.1"),
         "percent_of_beneficiaries_with_asthma":
             percent_of_beneficiaries_with_asthma_validator("2"),
         "state": state_validator("Enter the state:"),
         "asian_pacific_islander_beneficiaries":
             asian_pacific_islander_beneficiaries_validator("Enter the asian pacific islander beneficiaries:"),
         "hispanic_beneficiaries": hispanic_beneficiaries_validator("Enter the hispanic beneficiaries:")
         }
dataset_common_insert("111111", dataset)
