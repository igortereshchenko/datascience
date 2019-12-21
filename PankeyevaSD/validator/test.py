from PankeyevaSD.validator.lib import id_validator, zip_code_validator, percent_of_beneficiaries_with_copd_validator, percent_of_beneficiaries_with_hypertension_validator

id_key = "123456"
if id_validator(id_key):
    print("Id is correct")
else:
    print("Id is not correct, try again...")

zip_code = "12345"
if zip_code_validator(zip_code):
    print("zip_code is correct")
else:
    print("zip_code is not correct, try again...")

percent_with_copd = 45
if percent_of_beneficiaries_with_copd_validator(percent_with_copd):
    print("percent_of_beneficiaries_with_copd is not correct")
else:
    print("percent_of_beneficiaries_with_copd is not correct, try again...")

percent_with_hypertension = 69
if percent_of_beneficiaries_with_hypertension_validator(percent_with_hypertension):
    print("percent_of_beneficiaries_with_hypertension name is correct")
else:
    print("percent_of_beneficiaries_with_hypertension is not correct, try again...")
