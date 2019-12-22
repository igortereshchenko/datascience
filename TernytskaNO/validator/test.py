import TernytskaNO.validator.lib as lb

assert lb.spc_latin_validator("Platanus Arcius") == True
assert lb.spc_latin_validator("Platanus") == True
assert lb.spc_latin_validator("ulmus") == False

assert lb.status_validator("good") == True
assert lb.status_validator("not good") == False

assert lb.cen_year_validator("2006") == True
assert lb.cen_year_validator("20") == False

assert lb.wire_prime_validator("Yes") == True
assert lb.wire_prime_validator("No") == True
assert lb.wire_prime_validator("ye") == False
