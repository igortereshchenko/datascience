def recursion(dataset,i = 0):
    
    if len(dataset) > 0:
        keys = list(dataset.keys())
        agency_name = dataset[keys[i]]['agency_name']
        if dataset[keys[i]]['total_lupa_edisodes'] > 10 or dataset[keys[i]]['avarage_age'] > 40:
            print('Agency_name:' + str(agency_name) + '\nTotal_lupa_edisodes:' + str(dataset[keys[i]]['total_lupa_edisodes']))
        i += 1

    return(dataset,i)
