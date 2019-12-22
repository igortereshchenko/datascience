from GermanchukAV.dataset_structure import dataset

"""example of data"""
new_data = {
    '616777': {'country_code': 'US',
    'bed_type': 'Real Bed',
    'price': 300.0}
}

def add_new_dataset(dataset,new_data):
    dataset.update(new_data)
    print(dataset)

def is_instance(new_data):
    if isinstance(new_data, dict):
        add_new_dataset(dataset, new_data)
    else:
        print("Data is not valid")
is_instance(new_data)
