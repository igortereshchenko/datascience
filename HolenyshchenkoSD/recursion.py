# Function outputs state, percent_of_beneficiaries_with_cancer and percent_of_beneficiaries_with_depression if 
# percent_of_beneficiaries_with_cancer > 10 or percent_of_beneficiaries_with_depression > 20.

data_set = {
    '747203':
        {
            'state': 'TX',
            'percent_of_beneficiaries_with_cancer': 0,
            'percent_of_beneficiaries_with_depression': 62
        },
    '747016':
        {
            'state': 'TX',
            'percent_of_beneficiaries_with_cancer': 3,
            'percent_of_beneficiaries_with_depression': 71
        },
    '747145':
        {
            'state': 'TX',
            'percent_of_beneficiaries_with_cancer': 0,
            'percent_of_beneficiaries_with_depression': 47
        }}


def f(dct):
    for a in dct.items():
        if type(a[1]) == dict:
            f(a[1])
        elif a[0] == 'percent_of_beneficiaries_with_cancer' and a[1] > 10:
            print(dct)
        elif a[0] == 'percent_of_beneficiaries_with_depression' and a[1] > 20:
            print(dct)


f(data_set)
