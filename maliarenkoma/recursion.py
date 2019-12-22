import maliarenkoma.dataset_structure as ds


def number_of_cities_in(data: dict, year: int) -> int:
    if len(data) > 0:
        first_key = next(iter(data.keys()))
        element = data[first_key]

        my_sum = 0
        if element[ds.CEN_YEAR] == year:
            my_sum = len(element[ds.ZIP_CITY])

        data_clone = data.copy()
        data_clone.pop(first_key)
        return my_sum + number_of_cities_in(data_clone, year)
    else:
        return 0


print(number_of_cities_in(ds.dataset, 2001))
