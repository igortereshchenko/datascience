from budzinskiyeo.integration.dataset_structure_common import dataset
from budzinskiyeo.validator.lib import flavors_validator, count_validator, categories_validator, brand_validator
from miroshnyk_a_v.validator.lib import name_validator, reviews_validator, quantities_validator, sizes_validator


def dataset_insert(data, id_value, value_list, key_list=None):
    if key_list is None:
        key_list = ["count", "categories", "brand"]
    dictionary = dict()
    dictionary[id_value] = dict(zip(key_list, value_list))
    data.update(dictionary)


def recursion(valid_func, message, data=None, is_number=False, is_list=False, separator=None):
    """
    Recursion for validation function
    :param valid_func: name of validation function, function, count_validator
    :param message: (when data=None) prompt for input, str, "some message"
    :param data: data for valid, str, "some data" (when data=None func use the input to get str)
    :param is_number: flag for convert str to int, bool, True
    :param is_list: flag for convert str to list, bool, True
    :param separator: by which symbol list are separated (when separator=None => [space by default]), str, "s"
    :return: str/int, "123"/123
    """
    if data is None:
        data = input(message)
    if valid_func(data):
        if is_number:
            return int(data)
        else:
            if is_list:
                if separator is None:
                    separator = " "
                data = data.split(separator)
            return data
    else:
        return recursion(valid_func, message, is_number)


# My part of dataset
flavors = recursion(flavors_validator, "Enter flavors: ")
count = recursion(count_validator, "Enter count: ", is_number=True)
categories = recursion(categories_validator, "Enter categories: ", is_list=True)
brand = recursion(brand_validator, "Enter brand: ")

# Integration part of dataset
name = name_validator("Enter name: ")
sizes = sizes_validator("Enter sizes: ")
reviews = reviews_validator("Enter reviews: ")
quantities = quantities_validator("Enter quantities: ")

keys = ["count", "categories", "brand", "name", "sizes", "quantities", "reviews"]
values = [count, categories, brand, name, sizes, quantities, reviews]

dataset_insert(dataset, flavors, values, key_list=keys)

print(dataset)
