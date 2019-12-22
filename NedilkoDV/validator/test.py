from NedilkoDV.validator.lib import count_validator
from NedilkoDV.validator.lib import ID_validator
from NedilkoDV.validator.lib import key_validator
from NedilkoDV.validator.lib import brand_validator
from NedilkoDV.dataset_structure import dataset


ID=ID_validator(input('Введіть кодове позначення нового товару'))
count=count_validator(input('Введіть кількість товару на складі '))
brand=brand_validator(input('Введіть назву фірми'))
key=key_validator(input('Bведіть властивості товару'))
truekey=set(key.split())
print (truekey)
dataset[ID]={'count':count,
             'key':set(truekey),
               'brand':brand}
print(dataset)