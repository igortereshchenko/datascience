from DrobyazkoOV.intergration.dataset_structure_common import dataset


new = input("Enter id: ")
dataset[new] = {
    "name": {input("Enter name: ")},
    "prices.offer": {input("Enter prices: ")},
    "size": {input("Enter sizes: ")},
    "count": {input("Enter count: ")},
    "key": {input("Enter key: ")},
    "brand": {input("Enter brand: ")}
}
print(dataset)
