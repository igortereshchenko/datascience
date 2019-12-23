from dorotiuktimdt.validator.lib import ean_validator
from dorotiuktimdt.validator.lib import keys_validator
from dorotiuktimdt.validator.lib import manufacturer_validator
from dorotiuktimdt.validator.lib import brand_validator
from hudymvm.validator.lib import id_validator
from hudymvm.validator.lib import categories_validator
from hudymvm.validator.lib import name_validator
from dorotiuktimdt.integration.dataset_structure_common import dataset_integration

id = id_validator('Введіть id: ')
categories = categories_validator('Введіть категорію: ')
name = name_validator('Введіть назву товару: ')
keys = keys_validator()
brand = brand_validator()
manufacturer = manufacturer_validator()
ean = ean_validator()



dataset_integration["id"][id] = {'keys': keys, 'manufacturer': manufacturer, 'brand': brand, 'categories': categories, 'name': name, 'ean':ean
                                 }
print(dataset_integration)
