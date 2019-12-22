from SydorovaOS.dataset_structure import dataset

def count_zipcode(dataset,count,ind):
    if 1 in dataset.keys():
        dataset.pop(1)
        count+=1
        ind-=1
    ind+=1
    if ind >= len(dataset.keys()):
        return count
    else:
        return count_zipcode(dataset,count,ind)
count = 0
ind = 0
count = count_zipcode(dataset,count,ind)

print("Кількість дерев з zipcode = 1:",count)