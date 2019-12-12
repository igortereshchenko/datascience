from TitomyrOY.validator.lib import *

if name_validator("Handcrafted Alpaca Blend 'Purple Charisma' Sweater (Peru)"):
    print("Name is correct")
else:
    print("Name is incorrect")


if size_validator("38"):
    print("Size is correct")
else:
    print("Size is incorrect")


if weight_validator("0.499"):
    print("Weight is correct")
else:
    print("Weight is incorrect")


if features_validator(" "):
    print("Features are correct")
else:
    print("Features are incorrect")