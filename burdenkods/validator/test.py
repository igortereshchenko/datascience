import burdenkods.validator.lib as validator

assert validator.keys_validator("amazon.com") is True
assert validator.name_validator("Christian Louboutin, worn") is True
assert validator.asins_validator("") is True
assert validator.sizes_validator("7.5") is True
