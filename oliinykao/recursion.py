from oliinykao.dataset_structure import dataset

def get_key_list(dataset):
    list_of_keys = []
    for key in dataset.keys():
        list_of_keys.append(key)
    return list_of_keys

def recursion(dataset, list_of_keys, count = 0, brand_list = [], n = 0):
    if n >= len(dataset):
        return count
    else:
        if (dataset.get(list_of_keys[n]).get("colors") == "Red") & (dataset.get(list_of_keys[n]).get("brand") not in brand_list):
            count += 1
            brand_list.append(dataset.get(list_of_keys[n]).get("brand"))
        return recursion(dataset, list_of_keys, count, brand_list, n+1)

print(recursion(dataset, get_key_list(dataset)))