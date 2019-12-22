import Lanovenko.validator.lib as Lval
import Rodina.validator.lab as Rval

def dataset_common_insert(dataset):
    host_id = input("Host ID: ")
    while not Lval.host_id_validator(host_id):
        print("Expression is invalid! Try again")
        host_id = input("Host ID: ")
    else:
        host_id = int(host_id)

    beds = input("Beds: ")
    while not Lval.beds_validator(beds):
        print("Expression is invalid! Try again")
        beds = input("Beds: ")
    else:
        beds = int(beds)

    number_of_reviews = input("Number of reviews: ")
    while not Lval.number_of_reviews_validator(number_of_reviews):
        print("Expression is invalid! Try again")
        number_reviews = input("Numbers of reviews: ")
    else:
        host_id = int(number_of_reviews)

    country = input("Country: ")
    while not Lval.country_validator(country):
        print("Expression is invalid! Try again")
        country = input("Country: ")

    guests_included = input("Guests included: ")
    while not Rval.guests_included_validator(guests_included):
        print("Expression is invalid! Try again")
        guests_included = input("Guests included: ")
    else:
        guests_included = int(guests_included)

    room_type = input("Room type: ")
    while not Rval.room_type_validator(room_type):
        print("Expression is invalid! Try again")
        room_type = input("Room type: ")

    amenities = input("Amenities: ")
    while not Rval.amenities_validator(amenities):
        print("Expression is invalid! Try again")
        amenities = input("Amenities: ")

    dataset.update(host_id,
                   dict([('country', country),
                         ('beds', beds),
                         ('number_of reviews', number_of_reviews),
                         ('guests_included', guests_included),
                         ('room_type', room_type),
                         ('amenities', amenities)]))