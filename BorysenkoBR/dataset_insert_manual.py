from dataset_structure import dataset


def dataset_insert(dataset, provider_id, data, keys_list):
    new_data = dict(zip(keys_list, data))
    dataset.update({provider_id: new_data})


provider_id = '747429'
data = ['MISSOURI CITY', 4, 31]
keys_list = ["city", "percent_of_beneficiaries_with_osteoporosis", "percent_of_beneficiaries_with_schizophrenia"]
dataset_insert(dataset, provider_id, data, keys_list)
