def filtr(dct= dataset, filtered= {}):
    global a

    for i in dct.items():
        if type(i[1]) == dict:
            a = i[0]
            filtr(i[1], filtered)
        elif i[0] == 'state':
            state = {i[0]: i[1]}
        elif i[0] == 'percent_of_beneficiaries_with_cancer':
            cancer = {i[0]: i[1]}
            if i[1] > 10:
                filtered[a] = cancer

        elif i[0] == 'percent_of_beneficiaries_with_depression' and i[1] > 20:
            depression = {i[0]: i[1]}
            filtered[a] = state, cancer, depression

    return filtered
