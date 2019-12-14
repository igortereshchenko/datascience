# Function outputs state, percent_of_beneficiaries_with_cancer and percent_of_beneficiaries_with_depression if 
# percent_of_beneficiaries_with_cancer > 10 or percent_of_beneficiaries_with_depression > 20.


def filter(dct):
    for a in dct.items():
        if type(a[1]) == dict:
            filter(a[1])
        elif a[0] == 'percent_of_beneficiaries_with_cancer' and a[1] > 10:
            print(dct)
        elif a[0] == 'percent_of_beneficiaries_with_depression' and a[1] > 20:
            print(dct)


filter(data_set)
