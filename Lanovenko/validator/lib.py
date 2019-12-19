import re

def host_id_validator(host_id):
    return bool(re.match(r'^\d+$', host_id))

def country_validator(country):
    return bool(re.match(r'^([U][n][i][t][e][d] [S][t][a][t][e][s]){1}$', country))

def beds_validator(beds):
    return bool(re.match(r'^\d+$', beds))

def number_reviews_validator(number_reviews):
    return bool(re.match(r'^\d+$', number_reviews))