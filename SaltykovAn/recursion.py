from dataset_structure import dataset

def shows_parameters(dataset, i=0):
    if i == len(dataset):
        return False

    if dataset[i]['beds'] > 2 or dataset[0]['price'] > 100:
        print(dataset[i]['room_type'], '\n', dataset[i]['price'], '\n', dataset[i]['weekly_price'], sep='')
    shows_parameters(dataset, i + 1)

shows_parameters(dataset)
