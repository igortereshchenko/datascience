import csv

sHost = lambda sh: ' who is a super host!' if sh is 't' else '!'

with open('listings.csv', mode='r') as csv_file:
    f = open('description.txt', mode='w+')
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        f.write(f"There's an apartment in {row['street']} offered by {row['host_name']}{sHost(row['host_is_superhost'])}\r\n")