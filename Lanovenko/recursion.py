def recursion(dataset, i=0):

    if i == len(list(dataset.keys())):
        return

    host_id = list(dataset.keys())[i]
    country = dataset[host_id]['country']
    beds = dataset[host_id]['beds']
    number_of_reviews = dataset[host_id]['number_of_reviews']

    if number_of_reviews > 10 or beds > 1:
        print(country, host_id, beds)

    recursion(dataset, i+1)