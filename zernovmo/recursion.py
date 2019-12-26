example = [
    {'host_location': 'Seattle, Washington, United States',
     'host_is_superhost': False,
     'street': 'Gilman Dr W, Seattle, WA 98119, United States',
     'host_name': 'Maija'},
    {'host_location': 'Seattle, Washington, United States',
     'host_is_superhost': True,
     'street': 'Gilman Dr W, Seattle, NA 98119, United States',
     'host_name': 'Jill'},
    {'host_location': 'Seattle, Washington, United States',
     'host_is_superhost': False,
     'street': '7th Avenue West, Seattle, WA 98119, United States',
     'host_name': 'Emily'},
]


def iterate(d, i):
    obj = d[i]
    if obj['host_is_superhost'] is True or (obj['street'] in 'United States' and obj['street'] in 'WA'):
        print(obj)
    if i is not len(d)-1:
        iterate(d, i + 1)


iterate(example, 0)
