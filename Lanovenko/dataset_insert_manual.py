def dataset_insert_manual(dataset):
    host_id = int(input("Host ID: "))
    country = input("Country: ")
    beds = int(input("Number of beds: "))
    number_of_reviews = int(input("Number of reviews: "))

    dataset.update([(host_id, dict([('country', country), ('beds', beds), ('number_of_reviews', number_of_reviews)]))])