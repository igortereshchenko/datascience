def recursion(dataset, current_key = None):
    for key, value in dataset.items():
        if isinstance(value, dict):
            recursion(value, key)
        else:
            if key == 'city':
                temporary_city = value
            elif (key == 'percent_of_beneficiaries_with_hypertension' and int(value) > 20) or (key == 'percent_of_beneficiaries_with_osteoporosis' and int(value) > 30):
                print('\nprovider_id: ', current_key, '\ncity: ', temporary_city)


def data_input(dataset, new_id, new_city, new_hypertension, new_osteoporosis):
    dataset[new_id] = {'city': new_city, 'percent_of_beneficiaries_with_hypertension': new_hypertension, 'percent_of_beneficiaries_with_osteoporosis': new_osteoporosis}

recursion(test_dataset)

data_input(test_dataset, 397624, 'PITTSBURGH', 50, 10)