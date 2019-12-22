from dataset_structure import data_set

def rec(data_set,n=1):
    if n>len(data_set):
        return 0
    elif int(data_set[str(n)]["price"])>10 and int(data_set[str(n)]["price"])<100 :
        print(data_set[str(n)]["host-id"])
        print(data_set[str(n)]["bed-type"])
        print(data_set[str(n)]["price"])
    rec(data_set,n+1)