from hudymvm.dataset_structure import dataset
keys = list(dataset.keys())
length = len(keys)

def recursion(data, namecount, categoriescount, num):

    if num >= length:
        return 'success'

    id = keys[num]
    namelist = data[id]['name'].split()

    if len(namelist)<=3:
        print('Name <=3')
        return recursion(data, 0,0,num + 1)

    if data[id]['categories'] == []:
        print(id,'---',"Count of categories: ",categoriescount)
        return recursion(data, 0, 0, num + 1)

    else:
        categorieslist = data[id]['categories']
        categoriescount+=1
        data[id]['categories'] = categorieslist[1:]

        return recursion(data, namecount, categoriescount, num)

    return recursion(data, namecount, categoriescount, num + 1)

print(recursion(dataset, 0, 0, 0))