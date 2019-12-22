def filtr(dct, origdict, d):
    global a

    for i in dct.items():
        if type(i[1]) == dict:
            a = i[0]
            # print(i[0])
            filtr(i[1], dataset, d)
        elif i[0] == 'percent_of_beneficiaries_with_cancer' and i[1] > 10:
            # print(i, a)
            d[a] = i

        elif i[0] == 'percent_of_beneficiaries_with_depression' and i[1] > 20:
            # print(i, a)
            d[a] = i
    return d
