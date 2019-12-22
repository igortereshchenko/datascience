import rudiyov.validator.lib as vl1
from rudiyov.integration.dataset_structure_common import dataset
from uuid import uuid1
import PoliatskaAA.validator.lib as vl2


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


def get_ean(validator):
    """
    get ean
    :param validator: func with param str
    :return: str
    """
    ean = input("Введіть ean")
    if validator(ean):
        return ean
    else:
        print("Ви ввели не коректні данні.")
        return get_ean(validator)


def get_color(validator):
    """
    get color
    :param validator: func with param str
    :return: str
    """
    color = input("Введіть color")
    if validator(color):
        return color
    else:
        print("Ви ввели не коректні данні.")
        return get_color(validator)


def get_flavors(validator):
    """
        get flavors
        :param validator: func with param str
        :return: str
        """
    flavors = input("Введіть flavors")
    if validator(flavors):
        return flavors
    else:
        print("Ви ввели не коректні данні.")
        return get_flavors(validator)


def get_id(validator=None, data=dataset):
    """
    get id ,but if validator is absent create id with function uuid1
    :param validator: func
    :param data: dict, dataset
    :return: str,id
    """
    if validator is not None:
        uuid = input("Введіть ID або натисныть Enter тоді id зганеруться автоматично")
        if validator(uuid):
            if uuid not in data['id'].keys():
                return uuid
            else:
                print("Введений id не э унікальним")
                return get_id(validator)
        else:
            print("Ви ввели некоректні данні")
            return get_id(validator)
    else:
        return uuid1()


def push_information_into_base(data=dataset, one_id=None, price=None, brand=None, quantities=None, color=None, ean=None,
                               skus=None, flavors=None):
    data['id'][one_id] = {
        'price.count': price,
        'quantities': quantities,
        'brand': brand,
        'skus': skus,
        'ean': ean,
        'color': color,
        'flavors': flavors
    }


def main():
    price = get_price(vl1.pricecount_validator)

    brand = get_brand(vl1.brand_validator)
    quantities = get_quantities(vl1.quantities_validator)
    skus = get_skus(vl1.skus_validator)
    ean = get_ean(vl2.ean_validator)
    color = get_color(vl2.color_validator)
    flavors = get_flavors(vl2.flavor_validator)
    own_id = get_id(vl2.id_validator)
    push_information_into_base(dataset, own_id, price, brand, quantities, color, ean, skus, flavors)


main()
