from pavlovskaki.dataset_structure import dataset

"""
Function insert_line for adding information to the dataset.
The data has already written in the code.
"""

def insert_line(id_value, agency_name=None, street_adress=None, city=None, data=dataset):
    data[id_value] = {
        'agency_name': agency_name,
        'street_adress': street_adress,
        'city': city
    }


insert_line('368342', 'HEALTHY FOR YOU', '6029 ARROW HIGHWAY SUITE', 'HIALEAH')