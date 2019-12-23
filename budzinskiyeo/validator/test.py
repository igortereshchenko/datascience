from budzinskiyeo.validator.lib import flavors_validator, count_validator, categories_validator, brand_validator

flavor_key = "f158c2c9-ccde-4f5f-8ee4-bb070847f1b5"  # "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
count_value = "77"  # "123"
categories_value = ["Shoes", "Women"]  # ["element1", "element2"]
brand_value = ["Nora"]  # ["element1"]


if flavors_validator(flavor_key):
    print("Flavor id correct")
else:
    print("Invalid flavor id, try again")


if count_validator(count_value):
    print("Count value correct")
else:
    print("invalid count value, try again")


if categories_validator(categories_value):
    print("Categories list correct")
else:
    print("Invalid categories list, try again")


if brand_validator(brand_value):
    print("Brand list correct")
else:
    print("Invalid brand list, try again")
