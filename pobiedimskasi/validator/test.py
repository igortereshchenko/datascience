from pobiedimskasi.validator.lib import *

id = provider_id_validator()
state = state_validator()
depression = percent_of_beneficiaries_with_depression_validator()
hyperlipidemia = percent_of_beneficiaries_with_hyperlipidemia_validator()

print(id, '\n', state, '\n', depression, '\n', hyperlipidemia)
