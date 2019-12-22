import KoretsOleksandr.validator.lib as lib

assert lib.cen_year_validator("2005") is True
assert lib.cen_year_validator("19") is False

assert lib.vert_other_validator("Yes") is True
assert lib.vert_other_validator("yes") is False
assert lib.vert_other_validator("no") is True
assert lib.vert_other_validator("1") is False

assert lib.borocode_validator(0) is False
assert lib.borocode_validator(1) is True
assert lib.borocode_validator(6) is False

assert lib.key_validator('Kyiv') is True
assert lib.key_validator('kyiv') is False
assert lib.key_validator('K') is False
assert lib.key_validator('Kfikjhgfcvbnmfghj') is False