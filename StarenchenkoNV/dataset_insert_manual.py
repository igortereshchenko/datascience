from dataset_structure import dataset



def add_row(dataset,number_of_region,wire_prime_presence, info_about_shoes, sidw_crack_presence):
    """
    this func adds row to dataset
    """

    dataset[number_of_region] = {
        "wire_prime": wire_prime_presence
        ,"inf_shoes": info_about_shoes
        ,"sidw_crack": sidw_crack_presence
    }

    print(dataset)


add_row(dataset, "1", "No", "No", "No")