
def condition_depresion_more_than_50(key, value):
    c1 = (key == 'percent_of_beneficiaries_with_depression')
    if c1:
        c2 = int(value) > 50
        if c2:
            return True
    return False


def condition_hyperlipidemia_more_than_30(key, value):
    c1 = (key == 'percent_of_beneficiaries_with_hyperlipidemia')
    if c1:
        c2 = int(value) > 30
        if c2:
            return True
    return False


def recursion(dataset):
    if isinstance(dataset, dict):
        for key, value in dataset.items():
            if isinstance(value, dict):
                if recursion(value):
                    print('Provider ID: ' + str(key) + '\nState: ' + value['state'] + '\n')
            else:
                condition1 = condition_depresion_more_than_50(key, value)
                condition2 = condition_hyperlipidemia_more_than_30(key, value)
                if condition1 or condition2:
                    return True
        return False


recursion(dataset)