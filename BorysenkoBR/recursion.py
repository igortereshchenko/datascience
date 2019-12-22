def func2(dataset,n=0,keys_list=None):
    if keys_list==None:
        keys_list = list(dataset.keys())
        return func2(dataset,n,keys_list)
    if n==len(dataset):
        return
    if dataset[keys_list[n]]["percent_of_benefciaries_with_osteoporosis"]>5 and dataset[keys_list[n]]["percent_of_beneficiaries_with_schizophrenia"]> 15 :
        for elements in dataset[keys_list[n]]:
            print(elements + ' - '+ str(dataset[keys_list[n]][elements]))
    func2(dataset,n+1,keys_list)