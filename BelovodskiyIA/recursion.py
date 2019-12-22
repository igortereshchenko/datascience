dict_keys = list(data_structure.keys())


def show_data(data_structure, keys):
    if not len(keys):
        return False
    else:
        if 'phone' in data_structure[keys[0]]['host_verifications'] or data_structure[keys[0]]['state'] == 'WA':
            for k in data_structure[keys[0]].keys():
                if k != 'host_verifications':
                    print(data_structure[keys[0]][k])
            print('\n')
        return show_data(data_structure, keys[1:])


show_data(data_structure, dict_keys)