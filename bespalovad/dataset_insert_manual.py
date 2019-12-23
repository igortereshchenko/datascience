import dataset_structure

def dataset_insert_manual(ds):
	key = input ("Enter key: ")
	host_url = input ("Enter hosts URL: ")
	host_since = input ("Enter the time, since host is signed in: ")
	country = input ("Enter hosts country: ")
	zipcode = input ("Enter hosts zipcode: ")
	ds[key] = {}
	ds[key]['host_url'] = host_url
	ds[key]['host_since'] = host_since
	ds[key]['country'] = country
	ds[key]['zipcode'] = zipcode

def main():
	ds = dataset_structure.return_dataset()
	dataset_insert_manual(ds)
	return 0

if __name__ == '__main__':
	main()

