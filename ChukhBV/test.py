from validator import lib
while True:
    id=input("ID:")
    while not lib.validator_of_id(id):
        print("Something wrong with your input data. Try again:")
        id=input("ID:")
    else:
        id=int(id)
    neighbourhood=input("Neighbourhood:")
    while not lib.validator_of_neighbourhood(neighbourhood):
        print("Something wrong with your input data. Try again:")
        neighbourhood=input("Neighbourhood:")

    state=input("State:")
    while not lib.validator_of_state(state):
        print("Something wrong with your input data. Try again:")
        state=input("State:")

    market=input("Market:")
    while not lib.validator_of_market(market):
        print("Something wrong with your input data. Try again:")
        market=input("Market:")

    country=input("Country:")
    while not lib.validator_of_country(country):
        print("Something wrong with your input data. Try again:")
        country=input("Country:")


