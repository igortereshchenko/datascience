from olenchenkoma.dataset_structure import dataset

name=str(input("Введіть ім'я нового товару: "))
weight=int(input('Введіть вагу нового товару: '))
brand=str(input('Введіть назву бренду нового товару: '))
dimension=int(input('Bведіть розмір нового товару: '))
realname=set(name.split())

dataset[name]={'weight':weight,
               'brand':brand,
               'dimension': dimension
               }
print(dataset)