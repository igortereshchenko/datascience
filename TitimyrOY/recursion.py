def recursion(dataset, i):
    array = list(dataset.keys())
    if i < len(dataset):
        if len(array[i]) > 10:
            return recursion(dataset, i+1) + dataset[array[i]].get('weight')
    else:
        return 0
