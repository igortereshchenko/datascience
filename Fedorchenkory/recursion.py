from Fedorchenkory.dataset_structure import dataset
def recursion(dataset):
    summ=0
    key = (list(dataset.keys())).pop()
    new_dataset = dataset.get(key)
    if new_dataset.get('name') != None:
        summ += new_dataset.get('count')
    dataset.pop(key)
    if dataset != {}:
        summ += recursion(dataset)
    return summ
print(recursion(dataset))