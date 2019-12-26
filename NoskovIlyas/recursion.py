from NoskovIlyas.dataset_structure import data_set

def recursion(data_set, help_var):
        a = list(data_set.keys())
        key = 0
        if len(data_set)>0:
                key = a[0]
                if data_set[key]['cen_year'] == 2005:
                        help_var+=1
                        del data_set[key]
                else:
                        del data_set[key]
                return recursion(data_set,help_var)

        return help_var
print(recursion(data_set, 0))