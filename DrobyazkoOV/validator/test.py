from DrobyazkoOV.validator.lib import *

if name_validator("Boots"):
    print("correct")
else: print("not correct")

if id_validator("snsdk"):
    print("correct")
else: print("not correct")

if prices_offer_validator("456"):
    print("correct")
else: print("not correct")

if size_validator("23"):
    print("correct")
else: print("not correct")