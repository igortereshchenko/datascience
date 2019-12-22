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
        'wire_2nd': 222,
        'cen_year': 2018

    }

}

district_name = input("Какой район вы хотите добавить?\n")

def d_insert(db, district):
    if district in db:
        print("Район уже существует")
        return
    else:
        db[district] = dict()
        print("Район добавлен")
    return db

print(d_insert(city_info,district_name))
