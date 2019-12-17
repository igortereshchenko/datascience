import NoskovIlyas.dataset_structure as ds


def func4(data_set: dict, town: str, spc_common: dict, horz_grate: str, cen_year: int):
    data_set[town] = {
                    ds.Spc_common: spc_common,
                    ds.Horz_grate: horz_grate,
                    ds.Cen_year: cen_year
                    }



func4(ds.data_set, 'Staten Island', {'Linden, American'}, 'no', 2006)
print(ds.data_set)