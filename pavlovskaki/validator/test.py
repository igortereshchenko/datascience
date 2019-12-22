from pavlovskaki.validator.lib import id_validator, agency_name_validator, street_adress_validator, city_validator


id = "123456"                                 # 6 digits
agency_name = "RAINBOW HOME, INC"             # AGENCY NAME, INC
street_adress = "7754 BOURBON AVENUE"         # Number NAME OF STREET ADRESS
city = "MIAMI"                                # NAME OF CITY


if id_validator(id):
    print("Id is correct")
else:
    print("Id is not correct, please try again")


if agency_name_validator(agency_name):
    print("Agency name is correct")
else:
    print("Agency name is not correct, please try again")


if street_adress_validator(street_adress):
    print("Street adress is not correct")
else:
    print("Street adress is not correct, please try again")


if city_validator(city):
    print("City name is correct")
else:
    print("City name is not correct, please try again")