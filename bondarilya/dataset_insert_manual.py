from bondarilya.dataset_structure import dataset


def data_set_insert(data, id, value_list, key_list=None):
    if key_list is None:
        key_list = ["state", "other_unknown_beneficiaries", "percent_of_beneficiaries_with_alzheimers"]
    resdict = dict()
    resdict[id] = dict(zip(key_list, value_list))
    data.update(resdict)


provider_id = "237576"
values = ["MI", None, 8]

data_set_insert(dataset, provider_id, values)
print(dataset)
