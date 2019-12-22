import re


def name_validator(name):
	return bool(re.match("^[A-Z][a-z]+(( | - )([A-Z][a-z]+|\d+))*$", name))


def city_validator(city):
	return bool(re.match("^[A-Z][a-z]+((-| )[A-Z][a-z]+)*$", city))


def country_validator(country):
	return bool(re.match("^([A-Z][a-z]+((-| )[A-Z][a-z]+)*)|[A-Z]+$", country))


def country_code_validator(country_code):
	return bool(re.match("^[A-Z]+$", country_code))

