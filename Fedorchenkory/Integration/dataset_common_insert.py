from Fedorchenkory.Integration.dataset_structure_common import dataset
from Fedorchenkory.validator.lib import td_validator, name_validator, count_validator,reviews_validator
from dorotiuktimdt.validator.lib import manufacturer_validator,keys_validator,brand_validator
td = td_validator(input('enter id of ur product\n'))
name = name_validator(input('enter name of ur product\n'))
count = count_validator(input('enter name of ur product\n'))
reviews = reviews_validator(input('enter reviews of ur product\n'))
manufacturer = manufacturer_validator()
keys = keys_validator()
brand = brand_validator()
lib = {td:{'name':name,
            'count':count,
            'reviews':reviews,
            'manufacturer':manufacturer,
            'keys':keys,
            'brand':brand}
        }

dataset.update(lib)
print(dataset)