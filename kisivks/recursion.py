import kisivks.dataset_structure


def handle_data(data):
    if len(data) != 0:
        keys = list(data.keys())
        first_key = keys[0]
        value = data[first_key]
        if value['percent_of_beneficiaries_with_ra_oa'] > 10 or value['percent_of_beneficiaries_with_stroke'] > 20:
            print('provider_id: ' + str(first_key), 'zip_code: ' + str(value['zip_code']))

        updated_data = {}
        for i in range(1, len(keys)):
            updated_data[keys[i]] = data[keys[i]]

        handle_data(updated_data)


handle_data(kisivks.dataset_structure.dataset)

