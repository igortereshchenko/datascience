from pavlovskaki.dataset_structure import dataset

"""
    function main
    Condition:  city "Brea" or city "IRWINDALE".
    Print    :  "agency_name" and "street_adress"
                
"""

def main(dictionary, some_find_list, some_print_list):
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                main(value, some_find_list, some_print_list)
            else:
                if key == "city" and value in some_find_list:
                    for element in some_print_list:
                        print(dictionary[element])


find_list = ["BREA", "IRWINDALE"]
print_list = ["agency_name", "street_adress"]

main(dataset, find_list, print_list)