import re


def host_name_validator(text):

	if re.search(f'\s',text):

		return False, 'Not Correct input text.Spaces in it'

	else:

		return (True, ) if re.match(f'\w[A-Za-z0-9_]*',text) else (False, 'Not Correct input text')

def name_validator(text):

	if re.search(f'\s',text):

		return False, 'Not Correct input text.Spaces in it'

	else:

		return (True, ) if re.match(f'\w[A-Za-z0-9_]*',text) else (False, 'Not Correct input text')


def street_validator(text):

	if re.search(f'\s',text):

		return False, 'Not Correct input text.Spaces in it'

	else:

		return (True,) if re.match(f'\w[A-Za-z0-9_]*',text) else (False, 'Not Correct input text')



def host_response_time_validator(text):

	if re.search(f'\s',text):

		return False, 'Not Correct input text.Spaces in it'
	else:

		return (True,) if re.match(f'\d[0-9\.{1}\d[0-9]*]*',text) else (False, 'Not Correct input text')
