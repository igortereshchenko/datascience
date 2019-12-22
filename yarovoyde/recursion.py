def recursion(dataset, n=0,keys=[]):
    if keys==[]:
        keys = list(dataset.keys())
        return recursion(dataset, n, keys)
    if n==len(dataset):
        return None
    if dataset[keys[n]]["percent_of_beneficiaries_with_cancer"]>10 or 
    dataset[keys[n]]["percent_of_beneficiaries_with_diabetes"]> 50 or 
    (dataset[keys[n]]["percent_of_beneficiaries_with_cancer"]> 5 and 
     dataset[keys[n]]["percent_of_beneficiaries_with_diabetes"]> 20) :
        for elements in dataset[keys[n]]:
            print(elements + str(dataset[keys[n]][elements]))
    recursion(dataset,n+1,keys)
