import re


def host_id_validator(host_id):
    return bool(re.match(r'^\d+$', host_id))

def room_type_validator(room_type):
    return bool(re.match(r'^(Private room){1}$', room_type)) or bool(re.match(r'^(Entire home/apt){1}$', room_type))

def guests_included_validator(guests_included):
    return bool(re.match(r'^\d+$', guests_included))

def amenities_validator(amenities):
    amenities_list = ['Internet', 'TV', 'Cable TV', 'Wireless Internet', 'Air Conditioning', 'Heating', 'Washer',
                      'Dryer', 'Kitchen', 'Family/Kid Friendly',
                      'Smoke Detector', 'Carbon Monoxide Detector', 'Safety Card', 'Fire Extinguisher', 'Essantials',
                      'Shampoo', 'Indoor Fireplace', 'Free Parking pn Premises', 'Hot Tub', 'Dog(s)', 'Cat(s)',
                      'First Aid Kit', 'Buzzer/Wireless Intercom', 'Pets live on this property', 'Breakfast']
    for element in (re.split(', ', amenities)):
        if element not in amenities_list:
            return False
    return True