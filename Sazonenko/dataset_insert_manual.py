from Sazonenko.dataset_structure import dataset

new_line = {'TILIA AMERICANA':{'status': 'Dead',
                               'wire_htap': 'No',
                               'borocode': 5}}
dataset.update(new_line)
print(dataset)
