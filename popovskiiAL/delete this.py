import re
city_validator = r"[\w{2,10}]"
inputed = input("city")
while not re.match(city_validator, inputed) :
    inputed = input("city")
print(inputed)
