from dorotiuktimdt.validator.lib import ean_validator
from dorotiuktimdt.validator.lib import keys_validator
from dorotiuktimdt.validator.lib import manufacturer_validator
from dorotiuktimdt.validator.lib import brand_validator
from dorotiuktimdt.dataset_structure import dataset


ean = ean_validator()
keys = keys_validator()
manufacturer = manufacturer_validator()
brand = brand_validator()

dataset["ean"][ean] = {'keys': keys, 'manufacturer': manufacturer, 'brand': brand}
print(dataset)