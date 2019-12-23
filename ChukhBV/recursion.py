from dataset_structure import dataset
def recursion(dataset,n=0):
    while len(dataset.keys())!=n:
        id=list(dataset.keys())[n]
        neighbourhood = dataset[id]["neighbourhood"]
        state = dataset[id]["state"]
        market = dataset[id]["market"]
        country = dataset[id]["country"]
        if state == "WA" or neighbourhood == "Ballord":
            print("\nID:"+str(id) + "\nMarket:"+str(market)+"\nCountry:" + str(country)+"\nState:"+str(state))
        return recursion(dataset,n+1)

recursion(dataset)
