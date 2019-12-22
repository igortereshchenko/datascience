import maliarenkoma.validator.lib as lib

assert lib.cen_year_validator("2005") is True
assert lib.cen_year_validator("19") is False

assert lib.inf_other_validator("Yes") is True
assert lib.inf_other_validator("yes") is True
assert lib.inf_other_validator("no") is True
assert lib.inf_other_validator("1") is False

assert lib.spc_common_validator("PEAR, CALLERY") is True
assert lib.spc_common_validator("LINDEN, LITTLE LEAF") is True
assert lib.spc_common_validator("Linden, Ldsa, 25") is False

assert lib.zip_city_validator("Jamaica") is True
assert lib.zip_city_validator("Jamaica, Bronx") is True
assert lib.zip_city_validator("3420, 32") is False
