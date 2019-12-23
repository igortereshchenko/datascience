from KoretsOleksandr.dataset_structure import dataset

def recursin_func(dataset, help_var):
    '''
        рекурсія виводить скільки видів древ в бронксі
    :param dataset:
    :param help_var:
    :return:
    '''

    if len(dataset)>=1:
        if 'Bronx' in list(dataset.keys()):
            help_var = help_var + 1
            dataset.pop(list(dataset.keys())[0])
            return recursin_func(dataset, help_var)
        else:
            dataset.pop(list(dataset.keys())[0])
            return recursin_func(dataset, help_var)
    return help_var

print(recursin_func(dataset,0))