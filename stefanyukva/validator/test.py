import stefanyukva.validator.lib as lib

assert lib.boroname_validator("Text") is True
assert lib.boroname_validator("19") is False

assert lib.cb_num_validator("0") is True
assert lib.cb_num_validator("12") is True
assert lib.cb_num_validator("Boroname") is False
assert lib.cb_num_validator("00") is False

assert lib.st_accem_validator("0") is True
assert lib.st_accem_validator("12") is True
assert lib.st_accem_validator("Boroname") is False

assert lib.st_senate_validator("0") is True
assert lib.st_senate_validator("10") is True
assert lib.st_senate_validator("Boroname") is False