import re


def provider_id_validator(text):
    match = re.match('^\d{1,6}$', text)
    if match:
        # Чтоб не портить датасет, пусть уж лучше не будет ведущих нулей,
        # чем часть чисел будут str, часть int. Но вообще так работает:
        # if len(match.group()) < 6:
        #     print("0" * (6 - len(match.group())))
        #     return f'{"0" * (6 - len(match.group()))}{match.group()}'
        return int(match.group())
    else:
        print(f'\'{text}\' is not valid, must be up to 6 digits!')
        return None


def city_validator(text):
    match = re.match('[A-Z\s]+', text)
    if match:
        return match.group()
    else:
        print(f'\'{text}\' is not valid, must be capital word(-s)!')
        return None


def zip_code_validator(text):
    match = re.match('^\d{5}$', text)
    if match:
        return int(match.group())
    else:
        print(f'\'{text}\' is not valid, must be 5 digits!')
        return None


def total_episodes_non_lupa_validator(text):
    match = re.match('\d+', text)
    if match:
        return int(match.group())
    else:
        print(f'\'{text}\' is not valid, must be integer!')
        return None
