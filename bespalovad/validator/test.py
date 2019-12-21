import lib

def main():
	key = input ("Enter key: ")
	host_url = lib.host_url_validator(input ("Enter hosts URL: "))
	host_since = lib.host_since_validator(input ("Enter the time, since host is signed in: "))
	country = lib.country_validator(input ("Enter hosts country: "))
	zipcode = lib.zipcode_validator(input ("Enter hosts zipcode: "))
	print (key, ": host_url: ", host_url, ", host_since: ", host_since, ", country: ", country, ", zipcode: ", zipcode)
	return 0

if __name__ == '__main__':
	main()

