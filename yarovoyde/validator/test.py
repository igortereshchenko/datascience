from yarovoyde.validator.lib import *

provider_id = provider_id_validator("Input provider ID: ")
city = city_validator("Input city: ")
percent_of_beneficiaries_with_cancer = percent_of_beneficiaries_with_cancer_validator("Input percent of beneficiaries with cancer")
percent_of_beneficiaries_with_diabetes = percent_of_beneficiaries_with_diabetes_validator("Input percent of beneficiaries with diabetes: ")


dataset[provider_id] = {
    'city': city,
    'percent_of_beneficiaries_with_cancer': percent_of_beneficiaries_with_cancer,
    'percent_of_beneficiaries_with_diabetes': percent_of_beneficiaries_with_diabetes
}

print(dataset) 