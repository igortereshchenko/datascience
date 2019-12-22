from dataset_structure_common import dataset
import datascience.Lanovenko.validator.lib as lvl
import datascience.ChukhBV.validator.lib as cvl

def dataset_common_structure(dataset):
    id = input("ID:")
    while not cvl.validator_of_id(id):
        print("Something wrong with your input data. Try again:")
        id = input("ID:")

    host_id = input("Host ID: ")
    while not lvl.host_id_validator(host_id):
        print("Something wrong with your input data. Try again:")
        host_id = input("Host ID: ")

    beds = input("Number of beds: ")
    while not lvl.beds_validator(beds):
        print("Something wrong with your input data. Try again:")
        beds = input("Beds: ")

    number_of_reviews = input("Number of reviews: ")
    while not lvl.number_reviews_validator(number_of_reviews):
        print("Something wrong with your input data. Try again:")
        number_reviews = input("Numbers of reviews: ")

    neighbourhood=input("Neighbourhood:")
    while not cvl.validator_of_neighbourhood(neighbourhood):
        print("Something wrong with your input data. Try again:")
        neighbourhood=input("Neighbourhood:")

    state=input("State:")
    while not cvl.validator_of_state(state):
        print("Something wrong with your input data. Try again:")
        state=input("State:")

    market=input("Market:")
    while not cvl.validator_of_market(market):
        print("Something wrong with your input data. Try again:")
        market=input("Market:")

    country=input("Country:")
    while not cvl.validator_of_country(country):
        print("Something wrong with your input data. Try again:")
        country=input("Country:")

    dataset.update([(id,
                   dict([("host_id:", host_id),
                         ('beds:', beds),
                         ('number_of reviews:', number_of_reviews),
                         ('neighbourhood:', neighbourhood),
                         ('state:', state),
                         ('market:', market),
                         ('country:',country)]))])

dataset_common_structure(dataset)
print(dataset)