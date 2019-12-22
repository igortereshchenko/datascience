from dataset_structure import data_set


def print_data(data_set, counter=0):
    keys = list(data_set.keys())
    if counter < len(keys):
        if data_set[keys[counter]]['country_code'] == 'US' and len(data_set[keys[counter]]['city']) < 5:
            print([keys[counter]][0])
            print(data_set[keys[counter]]['city'])
            print(data_set[keys[counter]]['country'])
        print_data(data_set, counter+1)
    else:
        return True
