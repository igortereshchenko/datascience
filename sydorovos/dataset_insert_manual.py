import sydorovos.dataset_structure as syd

def insert(dataset: dict(), zip_city, st_assem, cen_year, horz_blck):

    var = dict()

    var['st_assem'] = st_assem

    var['horz_blck'] = horz_blck

    var['cen_year'] = cen_year

    dataset[zip_city] = var
    return dataset

print(insert(syd.dataset_/example, 1, 2, 3, 4))