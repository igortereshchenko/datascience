from dataset_structure import dataset

new = input("Enter id: ")
dataset[new] = {
    "name": {input("Enter name: ")},
    "prices.offer": {input("Enter prices: ")},
    "size": {input("Enter sizes: ")}
}