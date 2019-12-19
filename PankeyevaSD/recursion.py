from PankeyevaSD.dataset_structure import dataset
lst = list(dataset.keys())

def recursion(data):
    if len(data) == 0:
        return 0

    condition = 0
    for key, value in dataset[data[0]].items():
        if key == 'percent_of_beneficiaries_with_hypertension' and value != 'None':
            condition +=1
        elif key == 'percent_of_beneficiaries_with_copd' and int(value) > 10:
            condition +=1
        else: continue
    if condition == 2:
        print(dataset[data[0]].get('zip_code'))
        print(data[0])
        print(dataset[data[0]].get('percent_of_beneficiaries_with_copd'))

    data = data[1:]
    recursion(data)


recursion(lst)
