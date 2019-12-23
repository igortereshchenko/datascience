from dataset_structure import dataset

number_of_district = "0" #number of district we work with

keys = list(dataset[number_of_district].keys())


def recurtion_function(keys, dataset,number_of_district):
    if len(keys) == 0:
        return 1

    if keys[0] == "sidw_crack":

        if dataset[number_of_district]["sidw_crack"] == "No":
            print("there are 0 crack in district we work with")
            return 1

        elif dataset[number_of_district]["sidw_crack"] == "Yes":

            print("there are 1 crack in district we work with")

    recurtion_function(keys[1:], dataset, number_of_district)


recurtion_function(keys, dataset,number_of_district)
