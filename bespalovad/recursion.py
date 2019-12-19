import dataset_structure
import datetime

def recursion (ds, i):
	try:
		key = next(i)
		now = datetime.date.today()
		host_since = ds[key]['host_since'].split("-")
		then = datetime.date(int(host_since[0]), int(host_since[1]), int(host_since[2]))
		delta = now - then
		if (ds[key]['country'] == 'United States'):
			print (key, ": ", ds[key]['host_url'], " ", ds[key]['zipcode'], " ", ds[key]['country'])
		recursion (ds, i)
	except:
		return 0
	
def main():
	ds = dataset_structure.return_dataset()
	i = iter(ds)
	recursion(ds, i)
	return 0

if __name__ == '__main__':
	main()

