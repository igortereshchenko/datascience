def recursion(dataset, current_key = null):
    for key, value in dataset:
        if isinstance(value, dict):
            recursion(value, key)
        else:
            if key == 'city':
                temporary_city = value
            elif (key == 'percent_of_beneficiaries_with_hypertension' and int(value) > 20) or (key == 'percent_of_beneficiaries_with_osteoporosis' and int(value) > 30):
                print('\nprovider_id: ', current_key, '\ncity: ', temporary_city)