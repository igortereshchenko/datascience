from dataset_structure_common import new_dataset
import sys
sys.path.insert(0, '/home/nazar/programming/PycharmProjects/datascience/StarenchenkoNV/validator')
from lib import *

sidw_crack = sidw_crack_validator(str_regexp)

inf_shoes = inf_shoes_validator(str_regexp)

prime_wires = wire_prime_validator(str_regexp)

cb_num = cb_num_validator(num_regexp)

zip_city = zip_city_vatidator(city_regexp)

status = status_validator(status_regexp)

cen_year = cen_year_validator(num_regexp)

def add_row(sidw_crack, inf_shoes, prime_wires, cb_num, zip_city ,status, cen_year):
    """
    this func adds row to dataset
    """

    new_dataset[zip_city] = {
        "cb-num":  cb_num
        ,"cen_year": cen_year
        ,"wire_prime":prime_wires
        ,"sidw_crack": sidw_crack
        ,"status":status
        ,"inf_shoes" : inf_shoes
    }

    print(new_dataset)


add_row(sidw_crack, inf_shoes, prime_wires, cb_num, zip_city,status, cen_year)