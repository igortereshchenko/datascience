import kisivks.validator.lib as lib

assert lib.provider_id_validator('284080') is True
assert lib.provider_id_validator('') is False

assert lib.zip_code_validator('094787') is True
assert lib.zip_code_validator('cat') is False

assert lib.percent_of_beneficiaries_with_ra_oa_validator('100') is True
assert lib.percent_of_beneficiaries_with_ra_oa_validator('165') is False

assert lib.percent_of_beneficiaries_with_stroke_validator('95') is True
assert lib.percent_of_beneficiaries_with_stroke_validator('02') is False
