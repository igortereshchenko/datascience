from GermanchukAV.dataset_structure import dataset

def recursion(dataset):
    if len(dataset) == 0:
        return 0
    keys = list(dataset.keys())
    dict = list(dataset.values())

    condition = 0
    for key, value in dict[0].items():
        if key == 'country_code' and value == 'US' :
            condition += 1
        elif key == 'price' and 15<value<100:
            condition += 1
        else:
            continue
    if condition == 2:
        print(keys[0])
        print(dataset[keys[0]].get('price'))
        print(dataset[keys[0]].get('bed_type'))

    del dataset[keys[0]]
    recursion(dataset)
copy_of_dataset = dataset.copy()
recursion(copy_of_dataset)













