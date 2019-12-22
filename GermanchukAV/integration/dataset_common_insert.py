from lashtabegav.validator import *
from GermanchukAV.validator import *
from dataset_structure_common import *



def dataset_common_insert(dataset):


    host_id = input("input host id: ")
    while not host_id_validator(host_id):
        print("Not valid! Try again")
        host_id = input("Host ID: ")


    country_code = input("input country code ")
    while not country_code_validator(country_code):
        print("Not valid! Try again")
        country_code = input("country_code ")

    bed_type = input("input bed type: ")
    while not bed_type_validator(bed_type):
        print("Not valid! Try again")
        bed_type = input("Beds: ")


    price = input("input price: ")
    while not price_validator(price):
        print("Not valid! Try again")
        price = input("price: ")



    country = input("input country: ")
    while not country_validator(country):
         print("Not valid! Try again")
         country = input("input country: ")


    number_of_reviews = int(input("input number of reviews: "))
    while not number_of_reviews_validator(number_of_reviews):
        print("Not valid! Try again")
        number_reviews = int(input("Numbers of reviews: "))



    review_scores_value = int(input("review_scores_value: "))
    while not review_scores_value_validator(review_scores_value):
        print("Expression is invalid! Try again")
        review_scores_value = int(input("review_scores_value: "))



    input_data = {host_id: {
            'country_code': country_code,
            'bed_type': bed_type,
            'price': price,
            'country': country,
            'number_of_reviews': number_of_reviews,
            'review_scores_value': review_scores_value}
    }

    dataset.update(input_data)



dataset_common_insert(dataset)
print(dataset)







