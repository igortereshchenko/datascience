from KoretsOleksandr.dataset_structure import dataset

# def plus_new_structure(start_dataset,new_part_of_dataset):
#     start_dataset.update(new_part_of_dataset)
#     return start_dataset
# print(plus_new_structure(dataset,micro_dataset))

def appdate_dict(dataset:dict,cen_year:int,vert_other:str,boroname:int,borocode:str):
    dataset['cen_year'].append(cen_year)
    dataset['vert_other'].append(vert_other)
    dataset['borocode'].append(borocode)
    dataset['boroname'].append(boroname)
    return dataset

print(appdate_dict(dataset,2005,'no',123,'Kyiv'))