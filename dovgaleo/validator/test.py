from dovgaleo.validator import lib

provider_id = lib.provider_id_validator('123456')
city = lib.city_validator('123456')
zip_code = lib.zip_code_validator('123456')
total_ep = lib.total_episodes_non_lupa_validator('123456')

print('\n   VALUES\n')

print('id =', provider_id)
print('city =', city)
print('zip =', zip_code)
print('total =', total_ep)
