from kondrasova.dataset_structure import dataset

def recursion(dataset):
  for provider_id in dataset.keys():
    state = dataset[provider_id]['state']
    asian_pacific_islander_beneficiaries = float(dataset[provider_id]['asian_pacific_islander_beneficiaries'])
    hispanic_beneficiaries = (dataset[provider_id]['hispanic_beneficiaries'])
    divided = asian_pacific_islander_beneficiaries / float(hispanic_beneficiaries)
    if hispanic_beneficiaries == ' ':
        return dataset
    else:
        if divided > 0.2:
            del dataset[provider_id]
            print('Provider ID: '+ str(provider_id) +'\nstate ' + state + '\nasian_pacific_islander_beneficiaries' + str(asian_pacific_islander_beneficiaries) + "\n")
            return recursion(dataset)
  if len(dataset) == 0:
    return "finish"
