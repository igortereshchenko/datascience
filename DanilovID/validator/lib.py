import re
def room_type_validator(type):
	if re.match(r'[A-Z][a-z]*\s+(room|home/apt|apt/home)',type):
		return True
	else:
		return False

def bedrooms_validator(bedrooms):
	if re.match(r'^\d+$',bedrooms):
		return True
	else:
		return False

def host_id_validator(id):
	if re.match(r'^\d+$',id):
		return True
	else:
		return False

def country_validator(country):
	if re.match(r'^([A-Z]([a-z]*\s?))*$',country):
		return True
	else:
		return False
