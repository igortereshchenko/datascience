import updated_validator as uv
from copy import deepcopy

#Мой ТОПОР
def dataset_common_insert(data):
    help_data = deepcopy(data)

    new_raw_tup = dict.popitem(help_data)
    new_raw_tup1 = dict.popitem(new_raw_tup[1])

    key_first_priority = input('ведіть цифри (головний ключ у датасеті коллеги)')
    key_second_priority = input('введіть ім`я хоста')

    new_raw = {key_first_priority:{key_second_priority:new_raw_tup1[1]}}

    new_raw = uv.host_identity_validator(new_raw, key_first_priority, key_second_priority, 'host_identity', '')
    new_raw = uv.host_is_superhost_validator(new_raw, key_first_priority, key_second_priority, 'host_is_superhost', '')
    new_raw = uv.street_validator(new_raw, key_first_priority, key_second_priority, 'street', '')
    new_raw = uv.country_validator(new_raw, key_first_priority, key_second_priority, 'country', '')
    new_raw = uv.market_validator(new_raw, key_first_priority, key_second_priority, 'market', '')
    new_raw = uv.neighbourhood_validator(new_raw, key_first_priority, key_second_priority, 'neighbourhood', '')
    new_raw = uv.state_validator(new_raw, key_first_priority, key_second_priority, 'state', '')

    for i in range(7):
        atribute = input('введіть назву атрибуту')
        new_value = input('введіть значення атрибуту')
        new_raw = uv.host_identity_validator(new_raw, key_first_priority, key_second_priority, atribute, new_value)
        new_raw = uv.host_is_superhost_validator(new_raw, key_first_priority, key_second_priority, atribute, new_value)
        new_raw = uv.street_validator(new_raw, key_first_priority, key_second_priority, atribute, new_value)
        new_raw = uv.country_validator(new_raw, key_first_priority, key_second_priority, atribute, new_value)
        new_raw = uv.market_validator(new_raw, key_first_priority, key_second_priority, atribute, new_value)
        new_raw = uv.neighbourhood_validator(new_raw, key_first_priority, key_second_priority, atribute, new_value)
        new_raw = uv.state_validator(new_raw, key_first_priority, key_second_priority, atribute, new_value)

    data.update(new_raw)
    return data
