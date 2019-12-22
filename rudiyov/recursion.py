from rudiyov.dataset_structure import dataset


def get_value(database, search_key, searched_array):
    """
    update array with values by key
    :param database: dict , dataset
    :param search_key: name of wanted key
    :param searched_array:list, empty array
    :return:None
    """
    for key in database.keys():
        if key == search_key:
            searched_array.append(database[key])
        elif isinstance(database[key], dict):
            get_value(database[key], search_key, searched_array)


__quantities = list()
get_value(dataset, "quantities", __quantities)
__prices = list()
get_value(dataset, "prices.count", __prices)


def search_max_price(quantities=__quantities, prices=__prices):
    """
     search max price with some criteria
    :param data: dict ,dataset
    :param quantities: list, value of sourceURLs
    :param prices: list, value of prices.count
    :return: float , max of prices witch meet the criteria
    """
    price_array = list()
    diction = dict(zip(prices, quantities))
    for key, items in diction.items():
        if len(items["sourceURLs"]) > 10:
            price_array.append(key)
    print(max(price_array))
    return max(price_array)