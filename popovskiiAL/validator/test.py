from popovskiiAL.validator.lib import code_request, zip_city_request, borocode_request, nta_name_request, cb_num_request

code = code_request()
city = zip_city_request()
borocode = borocode_request()
nta_name = nta_name_request()
cb_num = cb_num_request()
print(code)
print(city)
print(borocode)
print(nta_name)
print(cb_num)
