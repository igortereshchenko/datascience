import TernytskaNO.dataset_structure as ds

def dataset_rec(dataset):
    if len(dataset) > 0:
        sum = 0
        data_key = next(iter(dataset.keys()))
        new_dict = dataset[data_key]
        if new_dict["cen-year"] == 2006:
            if new_dict["status"] == "good":
                sum += 1
        ds_copy = dataset.copy()
        ds_copy.pop(data_key)
        return sum + dataset_rec(ds_copy)
    else:
        return 0
rec_ds = ds.tree_census
result = dataset_rec(rec_ds)
print(result)

