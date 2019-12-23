from dataset_structure import dataset

def insert(dataset,year, horz_plant, vert_wall, sidw_raise):
    dataset.update({year:{
        "horz_plant":horz_plant,
        "vert_wall":vert_wall,
        "sidw_raise":sidw_raise
    }})
    return dataset


insert(dataset, 2015, "No", "No", "Yes")

print(dataset)

