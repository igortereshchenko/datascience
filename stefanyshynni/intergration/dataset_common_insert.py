from Fedorchenkory.validator.lib import name_validator, count_validator, reviews_validator, td_validator
from stefanyshynni.validator.lib import name_validator, brand_validator, sizes_validator, merchants_validator
from stefanyshynni.intergration.dataset_structure_common import dataset

id = td_validator()
brand = brand_validator()
name = name_validator()
count = count_validator()
sizes = sizes_validator()
reviews = reviews_validator()
merchants = merchants_validator()

dataset['id'][id] = {'brand': {brand: {'name': name, 'count': count, 'sizes': sizes, 'reviews': reviews, 'merchants': merchants}}}
print(dataset)