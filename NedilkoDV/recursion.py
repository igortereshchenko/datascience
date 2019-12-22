from NedilkoDV.dataset_structure import dataset

def Get_brands(dict,IDs,List_of=[],n=0):
    if len(IDs)<n+1:
        return List_of#returnes list of IDs
    index=IDs[n]
    a = dict.get(index)
    Valuable = a.get('brand')
    kek=len_check(Valuable)
    if kek is True:
        List_of.append(IDs[n])
    n += 1
    return Get_brands(dict,IDs,List_of,n)

def Counts(dict,IDs,List_counts=[],n=0):
    if len(IDs)<n+1:
        return List_counts#returnes list of counts
    a=dict.get(IDs[n])
    Valuable=a.get('count')
    List_counts.append(Valuable)
    n+=1
    return Counts(dict,IDs,List_counts,n)

def len_check(brand):
    if len(brand)>10:
        return True
    else:
        return False

def getID(counts,IDs):
     m=max(counts)
     i=counts.index(m)
     index=IDs[i]
     return index

def main(dataset):
    IDs=list(dataset.keys())
    brandsID=Get_brands(dataset,IDs)
    CountsList=Counts(dataset,brandsID)
    id=getID(CountsList,brandsID)
    return id


print('База даних: ' ,dataset)
print ('Індекс товару з найбільшою наявністю кількість символів у назві якого перевищує 10 ')
print(main(dataset))

