from bondarilya.dataset_structure import dataset

def recursion(dataset, count=0, keys_list=None):
    if keys_list is None:
        keys_list = list(dataset.keys())
    if count == len(dataset):
        return
    alzheimers = int(dataset[keys_list[count]]["percent_of_beneficiaries_with_alzheimers"]) > 30
    unknown = int(dataset[keys_list[count]]["other_unknown_beneficiaries"]) > 20
    if alzheimers or unknown :
        print("provider_id = "+ str(keys_list[count]))
        print("\n".join([ i + " = "  + str(dataset[keys_list[count]][i]) for i in dataset[keys_list[count]]  if not i is "percent_of_beneficiaries_with_alzheimers"]))
    return recursion(dataset, count + 1, keys_list)
recursion(dataset)
