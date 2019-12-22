import sydorovos.dataset_structure as syd

numb_blck = []
def rec(dataset:dict, count):
    finder = list(dataset.keys())
    if count > len(dataset)-1:
        return
    else:
        if syd.dataset_example[finder[count]].get('horz_blck') == 'Yes':
            numb_blck.append(1)
        rec(dataset, count+1)
    return sum(numb_blck)

print(rec(syd.dataset_example, 0))

