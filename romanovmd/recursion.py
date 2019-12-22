from romanovmd.dataset_structure import dataset

def amount_of_keys():
    amount = list()
    for key in dataset.keys():
        amount.append(key)
    return len(amount)

def recursive(data, list_of_all_sizes = []):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'sizes':
                list_of_sizes = value.split(',')
                list_of_all_sizes.append(list_of_sizes)
                list_of_all_sizes.sort(key=len)
                recursive(value, list_of_all_sizes)
            else:
                recursive(value)
    if len(list_of_all_sizes) == amount_of_keys():
        list_of_all_sizes.sort(key=len)
        for key in dataset.keys():
            if dataset[key]['sizes'].split(',') == list_of_all_sizes[len(list_of_all_sizes)-1]:
                return dataset[key]['id']

print(recursive(dataset))