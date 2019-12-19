import Maistruk.validator.lib as lib

print("\ninf-canopy test --> Yes = ", lib.inf_canopy_validator("Yes"))
print("inf-canopy test --> nope = ", lib.inf_canopy_validator("nope"), end="\n\n")

print("inf-shoes test --> No = ", lib.inf_shoes_validator("No"))
print("inf-shoes test --> yes = ", lib.inf_shoes_validator("yes"), end="\n\n")

print("zip-city test --> Bronx = ", lib.zip_city_validator("Bronx"))
print("zip-city test --> 11231241 = ", lib.zip_city_validator("11231241"))
print("zip-city test --> New York = ", lib.zip_city_validator("New York"))
print("zip-city test --> mariupol = ", lib.zip_city_validator("mariupol"), end="\n\n")

print("cb-num test --> 595 = ", lib.cb_num_validator("595"))
print("cb-num test --> abc = ", lib.cb_num_validator("abc"))
print("cb-num test --> 124 123 = ", lib.cb_num_validator("124 123"))
print("cb-num test --> pro100 = ", lib.cb_num_validator("pro100"))

assert lib.inf_canopy_validator("Yes") is True
assert lib.inf_canopy_validator("yes") is False

assert lib.inf_shoes_validator("No") is True
assert lib.inf_shoes_validator("nope") is False

assert lib.zip_city_validator("Bronx") is True
assert lib.zip_city_validator("mariupol") is False
assert lib.zip_city_validator("123321") is False
assert lib.zip_city_validator("New York") is True

assert lib.cb_num_validator("595") is True
assert lib.cb_num_validator("abcde") is False
assert lib.cb_num_validator("-348") is False
