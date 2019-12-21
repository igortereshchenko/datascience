from stefanyshynni.validator.lib import name_validator
from stefanyshynni.validator.lib import brand_validator
from stefanyshynni.validator.lib import sizes_validator
from stefanyshynni.validator.lib import merchants_validator
from stefanyshynni.dataset_structure import dataset

brand = brand_validator()
name = name_validator()
sizes = sizes_validator()
merchants = merchants_validator()

dataset["brand"][brand] = {'name': name, 'sizes': sizes, 'merchants': merchants}
print(dataset)