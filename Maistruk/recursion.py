import Maistruk.dataset_structure as mds

def canopy_counter(dataset, can_status):
    if len(dataset)>0:
        temp_key = next(iter(dataset.keys()))
        temp_dict = dataset[temp_key]
        user_sum = 0
        if temp_dict["inf-canopy"] == can_status:
            user_sum += 1
        ds_copy = dataset.copy()
        ds_copy.pop(temp_key)
        return user_sum + canopy_counter(ds_copy, can_status)
    else:
        return 0


temp_ds = mds.Trees_Set
result = canopy_counter(temp_ds["Bronx"], "Yes")
print(result)