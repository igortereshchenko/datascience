from LutakMV.dataset_structure import dt
print(dt)

sum_canopy = 0
def count_inf_conopy(dt, sum_canopy):
    value = dt.popitem()
    value_name = value[1].popitem()
    if value_name[1]['inf_canopy'] == 'Yes':
        sum_canopy += 1
    dt.update({value[0]: value[1]})
    if not value[1]:
        return sum_canopy
    else:
        return count_inf_conopy(dt, sum_canopy)


sum_canopy = count_inf_conopy(dt, sum_canopy)

if sum_canopy == 0:
    print('There isn\'t any canopied trees')
elif sum_canopy == 1:
    print('There is', sum_canopy, 'canopied trees')
else:
    print('There are', sum_canopy, 'canopied trees')