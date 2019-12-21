from dataset_structure_common import dataset
import sys

sys.path.append('../../KornienkoT/validator')
from lib import *

sys.path.append('../')
from validator.lib import *

def dataset_common_insert(dataset, host_id, new_dataset):
    attributes = new_dataset.keys()
    funcs = {'space' : space_validator,
            'street' : street_validator,
            'zipcode' : zipcode_validator,
            'price' : price_validator,
            'minimum_nights' : minimum_nights_validator,
            'weekly_price' : weekly_price_validator}
    for index in attributes:
        if not funcs[index](new_dataset[index]):
            return
    dataset[host_id] = new_dataset

host_id = 32713558
new_dataset = {
    'space' : 'This home encompasses the character that is so sought after on Queen Anne. It is a large Craftsman with a beautiful and private garden. The front porch, gourmet kitchen, master suite, basement tv/ga...',
    'street' : '1st Avenue West, Seattle, WA 98119, United States',
    'zipcode' : '98119',
    'price' : '450',
    'minimum_nights' : '6',
    'weekly_price' : '800'
    }

dataset_common_insert(dataset, host_id, new_dataset)