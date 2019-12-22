from dataset_structure import dataset
def dataset_insert_manual(dataset):
    id=int(input("Введіть ID:"))
    neighbourhood=input("Введіть значення для neighbourhood:")
    state=input("Введіть значення для state:")
    market=input("Введіть значення для market:")
    country=input("Введіть значення для country:")
    dataset.update([(id,dict([("neighbourhood",neighbourhood),("state",state),("market",market),("country",country)]))])
dataset_insert_manual(dataset)
print(dataset)