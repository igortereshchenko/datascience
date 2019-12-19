import re

pattern_provider_id=re.compile(r"\d+$")
pattern_city=re.compile(r"[a-zA-Z -]+$")
pattern_total_lupa_episodes=re.compile(r"\d+$")
pattern_average_age=re.compile(r"\d+$")

def provider_id_validator(pattern_provider_id, prompt):
	number=(validator(pattern_provider_id, prompt))
	while int(number)<=0 or len(number)!=6:
		print("Provider ID should consist of 6 digits !")
		number=(validator(pattern_provider_id, prompt))
	return int(number)

def validator(pattern, prompt):
	data=input(prompt)	
	while not bool (pattern.match(data)):
		data=input(prompt)
	return data

def city_validator(pattern_city, prompt):
	name=(validator(pattern_city, prompt))
	return name		

def total_lupa_episodes_validator(pattern_total_lupa_episodes, prompt):
	number=int(validator(pattern_total_lupa_episodes, prompt))
	while number<0:
		print("You should enter only positive numbers !")
		number=int(validator(pattern_total_lupa_episodes, prompt))
	return number

def average_age_validator(pattern_average_age, prompt):
	age=int(validator(pattern_average_age, prompt))
	while age<=0:
		print("Age must be greater than zero !")
		age=int(validator(pattern_average_age, prompt))
	return age










