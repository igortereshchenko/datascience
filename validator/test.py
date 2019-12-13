from olenchenkoma.validator.lib import name_validator
from olenchenkoma.validator.lib import weight_validator
from olenchenkoma.validator.lib import dimension_validator
from olenchenkoma.validator.lib import brand_validator
from olenchenkoma.dataset_structure import dataset

name=name_validator(input("Введіть ім'я нового товару латиницею: "))
weight=weight_validator(input('Введіть вагу нового товару у кг: '))
brand=brand_validator(input('Введіть назву бренду нового товару латиницею: '))
dimension=dimension_validator(input('Bведіть розмір нового товару: '))
realname=set(name.split())

dataset[name]={'weight':weight,
               'brand':brand,
               'dimension': dimension
               }
print(dataset)