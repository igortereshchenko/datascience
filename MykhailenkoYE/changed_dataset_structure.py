city_info ={
    "West Coast":{
        "status":"Excellent",
        "zip_city":"Brooklyn",
        "horz_plant":"No",
        "boroname":"5"
    },
    "New York":{
        "status":"Poor",
        "zip_city":"Bronx",
        "horz_plant":"Yes",
        "boroname":"Manhattan"
    },
    "Kiev":{
        "status": "Dead",
        "zip_city": "Bronx",
        "horz_plant":"No",
        "boroname":"Queens"

    },
    "Moscow":{
        "status": "Dead",
        "zip_city": "Whitestone",
        "horz_plant": "No",
        "boroname": "Brooklyn"

    }
}
for items in city_info:
    # print(city_info[items])
    for items2 in city_info[items]:
        if city_info[items][items2] =="Brooklyn":
            # print(city_info[items])
            # for element in city_info[items][items2]:
                print(items2)
    # if city_info[items]["boroname"]
    # == "Brooklyn":

