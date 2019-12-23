dataset = {956883:
               {"Entire home/apt":
                    {2:
                         {"TV","Cable TV","Internet","Wireless Internet","Air Conditioning",
                          "Kitchen,Heating","Family/Kid Friendly","Washer","Dryer"}}},
           326758:
               {"Private room":
                    {1:
                         {"Wireless Internet","Free Parking on Premises",
                          "Heating","Smoke Detector","Essentials","Shampoo"}}},
           4606439:
               {"Entire home/apt":
                    {1:
                         {"TV","Cable TV","Wireless Internet","Kitchen","Free Parking on Premises","Indoor Fireplace","Heating",
                          "Smoke Detector","Carbon Monoxide Detector","Fire Extinguisher","Essentials","Shampoo"}}}}

host_id = int(input("Host ID: "))
room_type = input("Type of apartment: ")
guests_included = int(input("Number of people in each room: "))
amenities = set(input("Amenities: ").split(', '))

dataset.update(dict([(host_id, dict([(room_type, dict([(guests_included, amenities)]))]))]))