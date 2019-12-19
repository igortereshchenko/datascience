from validator import lab

host_id = input("Host ID: ")
while not lab.host_id_validator(host_id):
    print("Error! Try again")
    host_id = input("Host ID: ")
else:
    host_id = int(host_id)

room_type = input("Type of apartment: ")
while not lab.room_type_validator(room_type):
    print("Error! Try again")
    room_type = input("Type of apartment: ")

guests_included = input("Number of people in each room: ")
while not lab.guests_included_validator(guests_included):
    print("Error! Try again")
    guests_included = input("Number of people in each room: ")
else:
    guests_included = int(guests_included)

amenities = input("Amenities: ")
while not lab.amenities_validator(amenities):
    print("Error! Try again")
    amenities = input("Amenities: ")
else:
    amenities = set(amenities.split(', '))