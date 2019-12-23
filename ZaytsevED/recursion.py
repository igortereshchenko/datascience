def recursion(dataset, count=0):
    if count < len(dataset):
        lst_keys = list(dataset.keys())
        if dataset[lst_keys[count]]['white_beneficiaries']/dataset[lst_keys[count]]['black_beneficiaries'] > 0.3:
            state = 'State: ' + dataset[lst_keys[count]]['state'] + ','
            white_beneficiaries = ' white beneficiaries: ' + str(dataset[lst_keys[count]]['white_beneficiaries']) + ','
            black_beneficiaries = ' black beneficiaries: ' + str(dataset[lst_keys[count]]['black_beneficiaries'])
            print(state, white_beneficiaries, black_beneficiaries)
        count += 1
        return recursion(dataset, count)