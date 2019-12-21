def recursion(dataset, i=0):

    if i == len(dataset.keys()):
        return

    host_id = list(dataset.keys())[i]
    room_type = list(dataset[host_id].keys())[0]
    guests_included = list(dataset[host_id][room_type])[0]
    amenities = dataset[host_id][room_type][guests_included]

    if guests_included > 1 and room_type == 'Private room':
        print(host_id)
        print(room_type)
        print(amenities)

    recursion(dataset, i+1)