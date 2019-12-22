import re


def validator(prompt_input, prompt_error, pattern):
    text = input(prompt_input)
    while not bool(pattern.match(text)):
        text = input(prompt_error)
    return text


def provider_id_vr():
    return validator("Input Provider ID: ","Sorry, provider ID must consist of 5 numbers. Try again", re.compile("^\d{6}$"))


def state_vr():
    return validator("Input state: ","Sorry, state must consist of 2 letters. Try again",re.compile("^\w{2}$")).upper()


def other_unknown_beneficiaries_vr():
    res = validator("Input other unknown beneficiaries (correct 0 or 'space = None'): ",
                    "Error.  Please try again",
                    re.compile("^[|0,\s |]$"))
    if res == " ":
        res = None
    return  res


def percent_of_beneficiaries_with_alzheimers_vr():
    res = validator("Input percent of beneficiaries with alzheimers: ",
                     "Percent must be a number between 0 and 100. Try again:",
                     re.compile("^\d{1,3}$"))
    while 0 > int(res) or int(res) > 100:
        print('Percent can not be higher than 100 or lower than 0.')
        res = validator("Input percent of beneficiaries with alzheimers: ",
                        "Percent must be a number between 0 and 100. Try again:",
                        re.compile("^\d{1,3}$"))
    return res
