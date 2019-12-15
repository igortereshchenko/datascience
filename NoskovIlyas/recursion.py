from NoskovIlyas.dataset_structure import data_set

def recursion(info,help):
    if len(info)>=1:
        if info[0]=='2005':
            help=help+1
            return recursion(info[1:], help)
        else:
            return recursion(info[1:],help)
    return help
print(recursion(data_set['cen_year'],0))