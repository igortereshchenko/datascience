from budzinskiyeo.dataset_structure import dataset


def dataset_insert(data, id_value, value_list, key_list=None):
    if key_list is None:
        key_list = ["count", "categories", "brand"]
    dictionary = dict()
    dictionary[id_value] = dict(zip(key_list, value_list))
    data.update(dictionary)


main_id = "37d139b6-471f-4e7d-a0b3-0c25acde52f6"
values = [101, ["Shoes", "Women's Shoes"], ["Novice"]]

dataset_insert(dataset, main_id, values)
print(dataset)
