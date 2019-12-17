from PotapenkoIV.validator.lib import cen_year_validator, tree_loc_validator, spc_latin_validator, horz_other_validator

if cen_year_validator(flavor_key):
    print("Correct")
else:
    print("Invalid list, try again")


if tree_loc_validator(count_key):
    print("Correct")
else:
    print("invalid list, try again")


if spc_latin_validator(categories_value):
    print("Correct")
else:
    print("Invalid list, try again")


if horz_other_validator(brand_value):
    print("Correct")
else:
    print("Invalid list, try again")
