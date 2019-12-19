import pandas as pd


my_data = pd.DataFrame({
    'host_name': ['Maija','Andrea','Jill','Emily'],
    'host_id_veryf': ['t','t','t','t'],
    'host_is_super': ['f','t','f','f'],
    'street': ['Gilman Dr W, Seattle, WA 98119, United States','7th Avenue West, Seattle, WA 98119, United States','West Lee Street, Seattle, WA 98119, United States','	8th Avenue West, Seattle, WA 98119, United States']
})

def druk_data_filu(data,n=0):
    try:
        data.loc[n]
    except KeyError:
        return print(data[['host_name','street']])
    if 'f' in data[['host_is_super','host_id_veryf']].loc[n].values:
        return druk_data_filu(data.drop([n]),n+1)
    else:
        return druk_data_filu(data,n+1)

druk_data_filu(my_data)