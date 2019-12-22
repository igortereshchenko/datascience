def recursion(keynum):
    if 20<dataset[keynum]['price']<500 or dataset[keynum]['bed-type']=='Real Bed':
        print(dataset[keynum]['name'])
        print(dataset[keynum]['price'])
        print(dataset[keynum]['country'])
        print('---------------------------')
    if keynum<3:
        recursion(keynum+1)
