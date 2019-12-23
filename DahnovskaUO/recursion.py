from DahnovskaUO.dataset_structure import dataset

def price_condition(key, value):
    cond = (key == 'price')
    if cond:
        cond2 = float(value)
        if cond2 in range(15, 100):
            return True
    return False

def recursion(dataset):
    if isinstance(dataset, dict):
        for key, value in dataset.items():
            if isinstance(value, dict):
                if recursion(value):
                    print('IStreet: ' + str(key) + '\nCity: ' + value['city'] + '\nPrice: ' + value['price'] + '\n')
            else:
                prices = price_condition(key, value)
                if prices:
                    return True
        return False

recursion(dataset)