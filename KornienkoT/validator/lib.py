import re

def host_id_validator(text):
    
    if re.match( r'^\d+$', text ): return True
    else: return False

def price_validator(text):
    if re.match( r'^\$\d+.?\d*$', text ): return True
    else: return False

def minimum_nights_validator(text):
    if re.match( r'^\d+$', text ): return True
    else: return False

def weekly_price_validator(text):
    if re.match( r'^\$\d+.?\d*$', text ): return True
    else: return False