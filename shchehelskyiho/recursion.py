import dataset_structure

def recursion(dataset, n = None):

    if n == None: n = len(dataset) - 1
    
    keys = list(dataset.keys())

    if n == -1: return None

    if dataset[keys[n]]['street'].find('WA') != -1 or dataset[keys[n]]['street'].find('US') != -1:
        print('street:', dataset[keys[n]]['street'], ' | zipcode: ', dataset[keys[n]]['zipcode'], ' | host_id:', keys[n], '\n')

    recursion(dataset, n-1)

recursion(dataset_structure.dataset)