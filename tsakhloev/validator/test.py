from lib import *

data = {
    
    host_id_validator: ['', '123as', '4124521'],
    cleaning_fee_validator: ['', '123.0', '123.0', '$123.0', '$123', '$123.00'],
    calendar_updated_validator: ['', 'yesterday', 'tomorrow', 'a day ago', '5 days ago', 'an hour ago', '1 eternity ago'],
    extra_people_validator: ['', '123.0', '123.0', '$123.0', '$123', '$123.00']

}

for func in data.keys():
    print( f'| Function: {func.__name__}\n' )
    for text in data[ func ]:
        print( f'Data: {text if text else None}\nResult: {func(text)}\n' )