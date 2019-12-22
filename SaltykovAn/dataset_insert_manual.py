from dataset_structure import dataset


def add_el(dataset, added_room_type, added_price , added_weekly_price,added_beds):
    dataset += [{ "room_type":added_room_type, "price":added_price, "weekly_price":added_weekly_price, "beds":added_beds}]
add_el(dataset,'Private room',35,'$816.00',0)

print(dataset)