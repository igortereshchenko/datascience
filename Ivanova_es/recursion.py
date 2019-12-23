import Ivanova_es.dataset_structure as d
l = list(d.dataset.keys())
def find_plant(inx, lnd, lnl):
    if lnd>0:
        if 'cen_year' in d.dataset[l[inx]]:
            if d.dataset[l[inx]]['cen_year']==2005:
                print(l[inx],d.dataset[l[inx]])
        find_plant(inx=inx + 1, lnd=lnd - 1, lnl=lnl - 1)

find_plant(0, len(d.dataset), len(l))
