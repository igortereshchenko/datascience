import MashyrAM.validator.lib as validator

assert validator.provider_id_validator("747429") is True
assert validator.city_validator("MISSOURI CITY") is True
assert validator.percent_of_beneficiaries_with_hypertension_validator("67") is True
assert validator.percent_of_beneficiaries_with_osteoporosis_validator("4") is True