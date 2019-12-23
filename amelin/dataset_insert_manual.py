import pandas as pd

my_data = pd.DataFrame({
    'host_name': ['Maija','Andrea','Jill','Emily'],
    'host_id_veryf': ['t','t','t','t'],
    'host_is_super': ['f','t','f','f'],
    'street': ['Gilman Dr W, Seattle, WA 98119, United States','7th Avenue West, Seattle, WA 98119, United States','West Lee Street, Seattle, WA 98119, United States','	8th Avenue West, Seattle, WA 98119, United States']
})

new_row = pd.DataFrame({
    'host_name': [input('ввудіть ім`я хота')],
    'host_id_veryf': [input('чи перевірено ід')],
    'host_is_super': [input('чи є хост супер')],
    'street': [input('введіть вулицю хоста')]
})

oper_result = my_data.append(new_row, ignore_index=True, sort=False)

print(oper_result)

