dict_keys = list(dataset.keys())


def show_data(dataset, keys):
    if not len(keys):
        return False
    else:
        if dataset[keys[0]]['host_response_time'] > 10 and dataset[keys[0]]['host_response_time'] < 50:
            for k in dataset[keys[0]].keys():
                if k != 'host_response_time':
                    print(dataset[keys[0]][k])
            print(keys[0])
            print('\n')
        return show_data(dataset, keys[1:])


show_data(dataset, dict_keys)