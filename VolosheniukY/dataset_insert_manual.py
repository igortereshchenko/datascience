from dataset_structure import data_set


def add_data(data_s, name, city, country, country_code):
    data_s.update({
        name: {
            "city": city,
            "country": country,
            "country_code": country_code
        }
    })
    return data_s


add_data(data_set, 'Royal Apartment of Jordan 3', 'Seattle', 'United States', 'US')
print(data_set)

