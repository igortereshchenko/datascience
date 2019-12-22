from bondarilya.validator.lib import *

id = provider_id_vr()
state = state_vr()
unknown = other_unknown_beneficiaries_vr()
alzheimers = percent_of_beneficiaries_with_alzheimers_vr()

print(id, '\n', state, '\n', unknown, '\n', alzheimers)