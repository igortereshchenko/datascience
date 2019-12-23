from torbaso.dataset_structure import dataset
#Датасет Данилевича
data_set={
    1:{
        'host-id':956883,
        'bed-type':'Real Bed',
        'price':85.00,
        'extra-people':5.00
    },
    2:{
        'host-id':5177328,
        'bed-type':'Real Bed',
        'price':150.00,
        'extra-people':0.00
    },



    3:{
        'host-id':16708587,
        'bed-type':'Real Bed',
        'price':975.00,
        'extra-people':25.00
        }

}

def dataset_structure_common(basedataset,addeddataset):
   for i in range(1,4):
       basedataset[i].update(addeddataset[i])
   return dataset


dataset_structure_common(dataset,data_set)
