import popovskiiAL.dataset_structure as dataset


def add_data(dataset: dict, zip_city: str, cb_num: int, borocode: int, boroname: str):
    dataset[zip_city] = {
                            'cb_num': cb_num,
                            'borocode': borocode,
                            'boroname': boroname
                          }


add_data(dataset.dataset, 'Staten Island', 0, 5, "Staten Island")
print(dataset.dataset)
