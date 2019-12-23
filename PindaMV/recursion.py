from PindaMV.dataset_structure import dataset
print(dataset)

sum_confl = 0

def confl_count(dataset, sum_confl):
    value = dataset.popitem()
    dataset.update({value[0]: value[1]})
    in_value = value[1].popitem()
    value[1].update({in_value[0]: in_value[1]})
    if in_value[0] == 2006:
        if value[1][in_value[0]]['inf_other'] == 'Yes':
            sum_confl += 1
    value[1].pop(in_value[0])
    if len(value[1])==0:
        dataset.pop(value[0])

    if len(dataset.keys()) == 0:
        return sum_confl
    else:
        return confl_count(dataset, sum_confl)

sum = confl_count(dataset, sum_confl)
print(sum)

