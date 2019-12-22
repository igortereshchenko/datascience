from hudymvm.integration.dataset_structure_common import dataset
from hudymvm.validator.lib import id_validator, categories_validator, keys_validator, name_validator
from TitomyrOY_validator_lib import size_validator, weight_validator, features_validator

id = id_validator('Enter id ')
categories = categories_validator('Enter categories (separator ",") ')
keys = keys_validator('Enter keys (separator ",") ')
name = name_validator('Enter name ')

size = input('Enter size ')
if size_validator(size):
    print("Size is correct")
else:
    print("Size is incorrect")
weight = input('Enter weight ')
if weight_validator(weight):
    print("Weight is correct")
else:
    print("Weight is incorrect")
features = input('Enter features ')
if features_validator(features):
    print("Features are correct")
else:
    print("Features are incorrect")

dataset.update({id: {'categories':categories, 'keys':keys, 'name':name, 'size':size, 'weight':weight, 'features':features}})
print(dataset)