from dovgaleo.dataset_structure import dataset


def insert_data(data, dataset):
    if not isinstance(dataset, dict):
        print('Your dataset is not valid!')
        return -1
    key = list(data.keys())[0]
    if not isinstance(data, dict) or len(data) != 1\
            or not isinstance(key, int) or len(data[key]) != 3:
        print('Your data is not valid!')
        return -1
    dataset.update(data)


#   data
my_friend = {
    123456: {
        'city': 'BROOKLYN',
        'zip_code': 11222,
        'total_episodes_non_lupa': 2570
    }
}

insert_data(my_friend, dataset)

#   is insert correct?:
for key, value in dataset.items():
    print('id', key, value)

