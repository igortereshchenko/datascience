from re import compile

int_pattern = compile( r'^\d+$' )

money_pattern = compile( r'^\$\d+.\d\d$' )

calendar_patterns = [ r'yesterday', r'tomorrow', r'^\d+| (weeks|months|days) ago$', r'^a (day|week|month) ago', r'an hour ago' ]
calendar_patterns = [ compile( pattern ) for pattern in calendar_patterns ]

def host_id_validator( text ):
    return True if int_pattern.match( text ) else False

def cleaning_fee_validator( text ):
    return True if text == '' or money_pattern.match( text ) else False

def calendar_updated_validator( text ):
    return True if text == '' or any( [ pattern.match( text ) for pattern in calendar_patterns ] ) else False

def extra_people_validator( text ):
    return True if text == '' or money_pattern.match( text ) else False