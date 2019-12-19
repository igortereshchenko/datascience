dataset = {956883:{'United Sates':{1:207}},
           239585:{'United States':{1:181}},
           2315558:{'United States':{2:41}}}

host_id = int(input("Host ID: "))
country = input("Country: ")
beds = int(input("Number of beds: "))
number_reviews = int(input("Number of reviews: "))

dataset.update(dict([(host_id, dict([(country, dict([(beds, number_reviews)]))]))]))