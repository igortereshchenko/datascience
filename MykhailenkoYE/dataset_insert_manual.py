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
print("Виберіть потрібний ключ для додавання нового рядка")
for city_info_my in city_info:
    print(city_info_my)
input_key = input("Виберіть ключ,до якого будемо додавати рядок:")
a = 0
for key in city_info:
    if input_key != key:
        print("")
    else:
        a =1
if a==1:
    input_text = input("Введіть ключ, який хочете додати у рядок:")
    input_data = input("Введіть значення до ключа:")
    if input_key == "Kiev" or input_key =="Moscow" or input_key == "New York" or input_key =="West Coast":
            my_dataset = {input_key: input_data}
            city_info[input_key][input_text] = input_data
            print(city_info)
else:
    print("Такого ключа не існує!")



