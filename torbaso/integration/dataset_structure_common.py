from torbaso.dataset_structure import dataset
from danylevichoo.dataset_structure import data_set

def dataset_structure_common(basedataset,addeddataset):
   for i in range(1,4):
       basedataset[i].update(addeddataset[i])
   return dataset


print(dataset_structure_common(dataset,data_set))
