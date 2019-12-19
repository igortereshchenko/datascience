from nadya.dataset_structure import dataset
counting=list(dataset.items())
length=len(counting)
first_index=0
second_index=1
listofvar=[]#list created for finding an appropriate value(in our case max weight, when a color is red)
def recursion(data, tamplate_key, tamplate_val, first_index,second_index):
    for key,value in data.items():
        for seckey,secvalue in value.items():
            if seckey==tamplate_key and tamplate_val in secvalue:
                return listofvar.append(max(value.get("weight"))),recursion(dict(counting[first_index:second_index]), "color", "Red",first_index+1,second_index+1)
            else:
                return recursion(dict(counting[first_index:second_index]),"color","Red",first_index+1,second_index=1)
recursion(dict(counting[first_index:second_index]),"color","Red",first_index,second_index)
print("Maximum weight for red items is",max(listofvar))

#функція виводить максимальне значення ваги, для всіх продуктів червоного кольору
