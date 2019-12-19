from stefanyshynni.dataset_structure import dataset

def recursion(dataset):
    keys = list()
    if isinstance(dataset, dict):
        for key, value in dataset.items():
            if isinstance(value, dict):
                if key == 'brand':
                    keys.append(list(value.keys()))

    index_key = list()

    for i in range(len(keys[0])):
        element = keys[0][i]
        element = ''.join(element.split())

        if len(element) > 10:
            index_key.append(i)

    number_sizes = list()

    for j in range(len(index_key)):
        brand = keys[0][index_key[j]]
        sizes = len(dataset["brand"][brand]["sizes"])
        number_sizes.append(sizes)

    index_max_brand = number_sizes.index(max(number_sizes))
    max_brand = keys[0][index_key[index_max_brand]]
    print('Бренд із максимальною кількістю розмірів:', max_brand)
    return keys

recursion(dataset)