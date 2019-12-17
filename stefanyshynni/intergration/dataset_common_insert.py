from Fedorchenkory.validator.lib import name_validator, count_validator, reviews_validator, td_validator
from stefanyshynni.validator.lib import name_validator, brand_validator, sizes_validator, merchants_validator
from stefanyshynni.intergration.dataset_structure_common import dataset

#id = 'AVpe_1SHLJeJML430GHj'
#brand_value = 'Vans'
#name = 'Vans'
#count = '123'
#sizes = '40, 41, 42'
#reviews = '35'
#merchants = 'Ebay.com'


def get_id():
    id = input('ID:')
    if td_validator(id):
        print("Id list correct")
        return id
    else:
        print('Invalid id list, try again')
        return get_id()


def get_brand():
    brand_value = input('Brand:')
    if brand_validator(brand_value):
        print("Brand list correct")
        return brand_value
    else:
        print('Invalid brand list, try again')
        return get_brand()


def get_name():
    name = input('Name:')
    if name_validator(name):
        print("Name list correct")
        return name
    else:
        print('Invalid name list, try again')
        return get_name()


def get_count():
    count = input('Count:')
    if count_validator(count):
        print('Count list correct')
        return count
    else:
        print('Invalid count list, try again')
        return get_count()


def get_sizes():
    sizes = input('Sizes:')
    if sizes_validator(sizes):
        print("Sizes list correct")
        return sizes
    else:
        print('Invalid sizes list, try again')
        return get_sizes()


def get_reviews():
    reviews = input('Reviews:')
    if reviews_validator(reviews):
        print('Reviews list correct')
        return reviews
    else:
        print('Invalid reviews list, try again')
        return get_reviews()


def get_merchants():
    merchants = input('Merchants:')
    if merchants_validator(merchants):
        print("Merchants list correct")
        return merchants
    else:
        print("Invalid merchants list, try again")
        return get_merchants()


id = get_id()
brand_value = get_brand()
name = get_name()
count = get_count()
sizes = get_sizes()
reviews = get_reviews()
merchants = get_merchants()

dataset['id'][id] = {'brand': {brand_value: {'name': name, 'count': count, 'sizes': sizes, 'reviews': reviews, 'merchants': merchants}}}
print(dataset)