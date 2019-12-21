import re


def host_name_validator(text):

	if re.search(f'\s',text):

		return False, 'Not Correct input text.Spaces in it'

	else:

		return (True, ) if re.match(f'\w[A-Za-z0-9_]*',text) else (False, 'Not Correct input text')




def host_verifications_validator(list_texts):

	for text in list_texts:

		if re.search('\s',text):

			return (False, 'Not Correct input text.Spaces in it')

		else:

			if not re.match('\w[A-Za-z]*',text):

				return False, 'Not correct input text'

	return True ,

def state_validator(text):

	if re.search(f'\s',text):

		return False, 'Not Correct input text.Spaces in it'

	else:

		return (True,) if re.match(f'\w[A-Za-z0-9_]*',text) else (False, 'Not Correct input text')



def market_validator(text):

	if re.search(f'\s',text):

		return False, 'Not Correct input text.Spaces in it'

	else:

		return (True, ) if re.match(f'\w[A-Za-z0-9_]*',text) else (False, 'Not Correct input text')
