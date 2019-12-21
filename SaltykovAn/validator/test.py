from lib import *

if room_type_validator("Entire home/apt"):
    print("The entered data is correct")
else:
    print("Sorry, your data are incorrect")

if price_validator("45"):
    print("The entered data is correct")
else:
    print("Sorry, your data are incorrect")

if weekly_price_validator("815.00"):
    print("The entered data is correct")
else:
    print("Sorry, your data are incorrect")

if beds_validator("41.7"):
    print("The entered data is correct")
else:
    print("Sorry, your data are incorrect")