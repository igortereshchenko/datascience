from PankeyevaSD.dataset_structure import dataset

lst = list(dataset.keys())

def recursion(data,acum=0):
    if acum >= len(data) :
        return 0
    if dataset[data[acum]]['percent_of_beneficiaries_with_hypertension'] != None and int(dataset[data[acum]]['percent_of_beneficiaries_with_copd']) > 10:
        print(dataset[data[acum]].get('zip_code'))
        print(data[acum])
        print(dataset[data[acum]].get('percent_of_beneficiaries_with_copd'))
    recursion(data,acum+1)


recursion(lst)