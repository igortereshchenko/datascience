from lib import *

def output(attribute, ds_correct, ds_incorrect, ds_of_functions):
    print('Атрибут:', attribute, '\nДані '+ str(ds_of_functions) + ':', ds_correct) if ds_of_functions else print('Дані '+ str(ds_of_functions) + ':', ds_incorrect, '\n')

ds_correct = {'zipcode': '98119', 'street': '8th Avenue West, Seattle, WA 98119, United States', 'space': 'I hope this space will make my guests feel like they (EMAIL HIDDEN)fortable, in a great location and peaceful for an ideal getaway.', 'host_id': '1452570'}
ds_incorrect = {'zipcode': 'abc12', 'street': 'Вулиця Політехнічна, 22###', 'space': 'It\'s an amazing flat.\n            The park is near.', 'host_id': 'My host_id is 1452570'}
ds_of_attributes = ds_correct.keys()
ds = [ds_correct, ds_incorrect]

for index, elem in enumerate(ds_of_attributes):
    for j in range(2):

        ds_of_functions = {
            0: zipcode_validator(ds[(j)][elem]),
            1: street_validator(ds[(j)][elem]),
            2: space_validator(ds[j][elem]),
            3: host_id_validator(ds[j][elem])}

        output(elem, ds_correct[elem], ds_incorrect[elem], ds_of_functions[index])