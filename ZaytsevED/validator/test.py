from ZaytsevED.validator.lib import *


provide_id = provide_id_validator(input('Input the 6-digit identification number for the home health agency: '))
state = state_validator(input('Input state where agency is located: '))
white_beneficiaries = white_beneficiaries_validator(input('Input number of non-Hispanic white beneficiaries: '))
black_beneficiaries = black_beneficiaries_validator(input('Input number of non-Hispanic black or African American beneficiaries: '))