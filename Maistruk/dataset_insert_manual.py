import Maistruk.dataset_structure as mds

def add(dataset, cb_num, inf_c, inf_s, zip_city="Bronx"):
    if zip_city not in dataset.keys():
        dataset.update(dict({zip_city: {}}))
    print(dataset)
    dataset[zip_city].update({
            cb_num: {
                "inf-canopy": inf_c
                , "inf-shoes": inf_s
            }
    })
#add(mds.Trees_Set, 312, "No", "No", "Brooklyn")
#add(mds.Trees_Set, 264, "Yes", "Yes", "Bronx")
#add(mds.Trees_Set, 319, "Yes", "No", "Brooklyn")
#print(mds.Trees_Set)