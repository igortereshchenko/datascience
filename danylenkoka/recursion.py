city_info = {
    'new_jercy' : {
        'vert_wall': True,
        'wire_2nd': 200,
        'tree_loc': dict(),
        'cen_year': 2018,
    },


    'brooklyn': {
        'vert_wall': False,
        'wire_2nd': 1,
        'tree_loc': dict(),
        'cen_year': 2006,
    },


    'jercy': {
        'wire_2nd' : 222,
        'cen_year' : 2018

    }

}

my_date = int(input("Введите год для поиска:\n"))

def sec_wires_count(dataset,year):
    total_sum = 0
    for attributes in dataset.values():
        if 'cen_year' in attributes:
            if attributes['cen_year'] == year:
                total_sum += attributes['wire_2nd']
    return total_sum

print('Количество проводов в указанном году:',sec_wires_count(city_info,my_date))