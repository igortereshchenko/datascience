from NoskovIlyas.dataset1 import data_set1

def recursion(info,help):
    if len(info)>=1:
        if info['Bronx']['cen_year']=='2005':
            help=help+1
            return recursion(info.pop(), help)
recursion(,0)