from lib import num_regexp, cb_num_validator, str_regexp, wire_prime_validator, inf_shoes_validator, sidw_crack_validator

sidw_crack_status = sidw_crack_validator(str_regexp)

shoes_status = inf_shoes_validator(str_regexp)

prime_wires_status = wire_prime_validator(str_regexp)

cb_num = cb_num_validator(num_regexp)

print(sidw_crack_status, prime_wires_status, shoes_status, cb_num)

