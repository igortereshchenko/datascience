from dataset_structure import dataset

counter = 0
key_list = list(dataset.keys())

def recursion(dataset, key_list, counter):
    if len(key_list)== 0:
        print("кількість стін: ",counter)
        return 1

    if dataset[key_list[0]] == 2005 and dataset[key_list[0]]["vert_wall"] =="Yes":
        counter += 1

    recursion(dataset, key_list[1:], counter)


recursion(dataset, key_list, counter)