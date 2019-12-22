from burdenkods.dataset_structure import ShoeData

longnames = 0


def longnamecheck(data,iter,nameamount=0):
    i = 0
    for elem in data.values():
        if iter >i:
            i+=1
            continue
        elif len(elem['name'])>= 10:
            print(elem['name'])
            nameamount+=1
            i+=1
        longnamecheck(data, i, nameamount=nameamount)
        break
    if iter == len(data):
        print(nameamount)




longnamecheck(ShoeData, 0)
# recursion - if len(name) > 10:
# counter+=1
