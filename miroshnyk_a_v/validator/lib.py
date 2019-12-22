import re
def name_validator(prompt):
    print(prompt)
    text = input()
    while not bool(re.match('^.+$', text)):
        text = input(prompt)
    return text
def reviews_validator(prompt):
    print(prompt)
    text = input()
    while not bool(re.match('^.*$', text)):
        text = input(prompt)
    if text=="":
        return
    else:
        return text
def quantities_validator(prompt):
    print(prompt)
    number = input()
    while not bool(re.match('^\d*$', number)):
        number = input(prompt)
    if number == "":
        return
    else:
        return int(number)
def sizes_validator(prompt):
    plusX =0
    print(prompt)
    numbers = input()
    while not bool(re.match("^(\d\d?(\.\d)?(M|(\sX))?\s)*(\d\d?(\.\d)?(M|(\sX))?)?$",numbers)):
        numbers = input(prompt)
    numbers=numbers.split()
    for numb in numbers:
        if numb=="X":
            numbers.insert(plusX-1,numbers.pop(plusX-1)+" "+numbers.pop(plusX-1))
        plusX=plusX+1
    if numbers == []:
        return
    else:
        return numbers
def update(data):
    data.update({
        name_validator("Введіть поле name: "):{
             'sizes':sizes_validator("Введіть поле sizes числами через пробіл: "),
             'quantities':quantities_validator("Введіть поле quantities: "),
             'reviews':reviews_validator("Введіть поле reviews: ")}})