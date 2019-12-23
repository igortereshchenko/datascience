from DahnovskaUO.dataset_structure import dataset

new = {
    '8th Avenue West, Seattle, WA 98119, United States':
        {
        'country_code': 'US',
        'city': 'Seattle',
        'price': '100.00'
        }
}

def insert_info(dict):
    dataset.update(dict)

insert_info(new)
