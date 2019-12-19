import re
def status_validator(text):
    return bool(re.match(r'^[o,O]ld$|^[n,N]ew$',text))
def inf_shoes_validator(text):
    return bool(re.match(r'^[n,N]o$|^[y,Y]es$',text))
def zipcode_validator(text):
    text = str(text)
    return bool(re.match(r'^\d+$',text))
def trunk_dmg_validator(text):
    return bool(re.match(r'^[n,N]one$|^[c,C]avity$|^[t,T]runk [w,W]ound$|^[t,T]orn [b,B]ark$',text))