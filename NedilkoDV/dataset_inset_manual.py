from NedilkoDV.dataset_structure import dataset


ID=str(input('Введіть кодове позначення нового товару'))
count=int(input('Введіть кількість товару на складі '))
brand=str(input('Введіть назву фірми'))
key=str(input('Bведіть властивості товару'))
truekey=set(key.split())
print (truekey)
dataset[ID]={'count':count,
             'key':set(truekey),
               'brand':brand}
print(dataset)