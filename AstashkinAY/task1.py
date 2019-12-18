import csv

with open('listings.csv', mode='r') as csv_file:
    f = open('description.txt', mode='w+')
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        f.write(f"There's an apartment named {row['name']} with an unique id of {row['id']} offered by {row['host_name']} who's working with Airbnb since {row['host_since']}\r\n")