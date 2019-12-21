from hudymvm.dataset_structure import dataset
from hudymvm.validator.lib import id_validator, name_validator, categories_validator, keys_validator

id = id_validator('Enter id ')
categories = categories_validator('Enter categories (separator ",") ')
keys = keys_validator('Enter keys (separator ",") ')
name = name_validator('Enter name ')

dataset.update({id: {'categories':categories, 'keys':keys, 'name':name}})
print(dataset)
