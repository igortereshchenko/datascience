import re

def host_url_validator (s):
	if bool(re.match(r'(https://www.airbnb.com/users/show/)\d*\Z', s)):
		return s
	return None
	
def host_since_validator (s):
	if bool(re.match(r'\d{4}-\d{2}-\d{2}\Z', s)):
		return s
	return None
	
def country_validator (s):
	if bool(re.match(r'\D+\Z', s)):
		return s
	return None
	
def zipcode_validator (s):
	if bool(re.match(r'\d{5}\Z', s)):
		return s
	return None

