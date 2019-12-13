from dataset_struct import dataset


def recursion(dataset, count=0):
    if count in range(len(dataset.keys())):
        lst_keys = list(dataset.keys())
        num = dataset[lst_keys[count]]['white_beneficiaries']/dataset[lst_keys[count]]['black_beneficiaries']
        if num > 0.3:
            print(dataset[lst_keys[count]])
        count += 1
        recursion(dataset, count)


recursion(dataset)