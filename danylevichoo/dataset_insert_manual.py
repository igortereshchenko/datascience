from dataset_structure import data_set
from validator.lib import *

new = {
    str(len(data_set)+1):
        {
        "host-id": 123456789,
        "bed-type": 'Real Bed',
        "price": 100.00,
        "extra-people": 5.00
        }
}

def insert_info(dict):
    data_set.update(dict)

insert_info(new)
print (data_set)

"""
def insrt(data_set):
    data_set[len(data_set)+1] = {
        "host-id": input("Enter host-id: "),
        "bed-type": input("Enter type of bed: "),
        "price": input("Enter price: "),
        "extra-people": input("Enter sizes: ")
    }
"""