from olenchenkoma.validator.lib import name_validator, weight_validator, brand_validator, dimension_validator
from olenchenkoma.integration.dataset_structure_common import dataset
from romanovmd.validator.lib import id_validator, price_amountMin_validator, sizes_validator
def get_price(prompt):
    price = input(prompt)
    while not price_amountMin_validator(price):
        price = input(prompt)
    return str(price)

def get_id(prompt):
    id = input(prompt)
    while not id_validator(id):
        id = input(prompt)
    return str(id)

def update_dataset():
    dimension = dimension_validator("Введіть розмір - ")
    id = id_validator("Введіть id - ")
    name = name_validator("Введіть name - ")
    price_amountMin = price_amountMin_validator("Введіть price_amountMin - ")
    sizes = sizes_validator("Введіть sizes - ")
    dataset.update({id:{'id': id, 'dimension': dimension, 'name': name, 'price.amount_Min': price_amountMin, 'sizes': sizes}})
    print(dataset)

print(update_dataset())