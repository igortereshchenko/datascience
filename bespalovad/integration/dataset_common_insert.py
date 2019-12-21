import dataset_structure_common
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

def host_id_validator(data):
    match = re.match('^\d{4,8}$', data)
    if match:
        return int(match.group())
    else:
        print('This data is not valid')


def country_code_validator(data):
    match = re.match('^[A-Z]+$', data)
    if match:
        return match.group()
    else:
        print('This data is not valid')


def bed_type_validator(data):
    match = re.match('^[A-Z]([a-z-])+(\s[A-Z][a-z]+)*$', data)
    if match:
        return match.group()
    else:
        print('This data is not valid')

def price_validator(data):
    match = re.match('^\d+.\d+$', data)
    if match:
        return float(match.group())
    else:
        print('This data is not valid')

def dataset_insert_common(ds):
	key = input ("Enter key: ")
	host_url = host_url_validator(input ("Enter hosts URL: "))
	host_since = host_since_validator(input ("Enter the time, since host is signed in: "))
	country = country_validator(input ("Enter hosts country: "))
	zipcode = zipcode_validator(input ("Enter hosts zipcode: "))
	host_id = host_id_validator(input ("Enter hosts ID: "))
	country_code = country_code_validator(input ("Enter hosts country code: "))
	bed_type = bed_type_validator(input ("Enter bed type: "))
	price = price_validator(input ("Enter price: "))
	ds[key] = {}
	ds[key]['host_url'] = host_url
	ds[key]['host_since'] = host_since
	ds[key]['country'] = country
	ds[key]['zipcode'] = zipcode
	ds[key]['host_id'] = host_id
	ds[key]['country_code'] = country_code
	ds[key]['bed_type'] = bed_type
	ds[key]['price'] = price
	

def main():
	ds = dataset_structure_common.return_dataset()
	dataset_insert_common(ds)
	return 0

if __name__ == '__main__':
	main()

