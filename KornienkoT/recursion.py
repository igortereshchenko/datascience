from dataset_structure import dataset

def recursion(dataset, n = None):
    if n == None:
        n = len(dataset) - 1

    keys = list( dataset.keys() )

    data = dataset[ keys[n] ]
    price = data['price']
    minimum_nights = data['minimum_nights']
    weekly_price = data['weekly_price']


    if (price > 50 and price < 100) or weekly_price < 1000:
        print( 'host_id: ' + keys[n] + ', price: ' + price + ', minimum_nights: ' + minimum_nights + ', weekly_price: '+ weekly_price )

    if n == 0: return

    recursion( dataset, n - 1 )

recursion( dataset )