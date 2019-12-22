import TitomyrOY.validator.lib as val1
import rudiyov.validator.lib as val2
from TitomyrOY.integration.dataset_structure_common import dataset


def get_name(validator):
    """
    get value of name
    :param validator: func with param str
    :return: str
    """
    name = input("Введіть name")
    if validator(name):
        return name
    else:
        print("Ви ввели не коректні данні.")
        return get_name(validator)


def get_size(validator):
    """
    get value of size
    :param validator: func with param str
    :return: float
    """
    size = input("Введіть size")
    if validator(size):
        return size
    else:
        print("Ви ввели не коректні данні.")
        return get_size(validator)


def get_weight(validator):
    """
    get value of weight
    :param validator: func with param str
    :return: float
    """
    weight = input("Введіть weight")
    if validator(weight):
        return weight
    else:
        print("Ви ввели не коректні данні.")
        return get_weight(validator)


def get_features(validator):
    """
    get value of brand
    :param validator: func with param str
    :return: str
    """
    features = input("Введіть features")
    if validator(features):
        return features
    else:
        print("Ви ввели не коректні данні.")
        return get_features(validator)


def get_brand(validator):
    """
    get value of brand
    :param validator: func with param str
    :return: str
    """
    brand = input("Введіть brand")
    if validator(brand):
        return brand
    else:
        print("Ви ввели не коректні данні.")
        return get_brand(validator)



def get_price(validator):
    """
    get value of price
    :param validator: func with param str
    :return:float,price
    """
    price = input("Введіть price.count")
    if validator(price):
        return float(price)
    else:
        print("Ви ввели не коректні данні.")
        return get_price(validator)


def get_quantities(validator):
    """
    get dict - quantities
    :param validator: func with param str
    :return:dict , quantities
    """
    print("Введіть складові quantities")
    dataSeen = input("введіть дату елементи ввести через пробіл ").split()
    sourceURLs = input("введіть посилання")
    value = input("введіть значення")
    quantities = {
    'dateSeen': dataSeen,
    'sourceURLs': sourceURLs,
    'value': value
    }
    if validator(quantities):
        return dict(quantities)
    else:
        print("Ви ввели не коректні данні.")
        return get_quantities(validator)


def get_skus(validator):
    """
    get dict - skus
    :param validator: func with param str
    :return: dictionary
    """
    print("Введіть складові skus")
    sourceURLs = input("введіть посилання")
    value = input("введіть значення")
    skus = {
        'sourceURLs': sourceURLs,
        'value': value
    }
    if validator(skus):
        return dict(skus)
    else:
        print("Ви ввели не коректні данні.")
        return get_skus(skus)


def combine_information(data=dataset, name=None, price=None, brand=None, quantities=None, size=None, weight=None,
                               skus=None, features=None):
    data[name] = {
        'size': size,
        'weight': weight,
        'features': features,
        'brand': brand,
        'price.count': price,
        'quantities': quantities,
        'skus': skus,
    }


def main():
    name = get_name(val1.name_validator)
    size = get_size(val1.size_validator)
    weight = get_weight(val1.weight_validator)
    features = get_features(val1.features_validator)
    brand = get_brand(val2.brand_validator)
    price = get_price(val2.pricecount_validator)
    quantities = get_quantities(val2.quantities_validator)
    skus = get_skus(val2.skus_validator)
    combine_information(dataset, name, size, weight, features, brand, price, quantities, skus)

main()
print(dataset)