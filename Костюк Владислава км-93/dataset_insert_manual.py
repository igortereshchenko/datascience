from dataset_structure import data


def dataset_insert(dataset, provider_id, data, keys_list):
    new_data = dict(zip(keys_list, data))
    dataset.update({provider_id: new_data})


provider_id = '747429'
data = [77459,54,8]
keys_list = ["zip_code","average_age","percent_of_beneficiaries_with_stroke"]
dataset_insert(data, provider_id, data, keys_list)