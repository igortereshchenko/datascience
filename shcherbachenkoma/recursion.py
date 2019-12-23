def recursion(dataset_copy):
    if len(dataset_copy) == 0:
        return None
    else:
        for provider_id in dataset_copy.keys():
            agancy_name = dataset_copy[provider_id]['agency_name']
            average_hcc_score = float(dataset_copy[provider_id]['average_hcc_score'])
            condition1 = float(dataset_copy[provider_id]['average_hcc_score']) > 2
            condition2 = int(dataset_copy[provider_id]['percent_of_beneficiaries_with_asthma']) > 20
            if condition1 or condition2:
                del dataset_copy[provider_id]
                print('Provider ID: '+ str(provider_id) +'\nAgency name: ' + agancy_name+'\nAverage hcc score:' + str(average_hcc_score) + "\n")
                return recursion(dataset_copy)
