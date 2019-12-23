
import re
def count_validator():
    count = input('Введіть кількість одиниць товару:')
    if  bool(re.match('^[1-9]{1}[0-9]*$',count)):
        pass
    else:
        print('Неправильно введено кількість одиниць товару')
        return count_validator()
    return count


def name_validator():
    name = input("Введіть назву:")
    if bool(re.match("^(([A-Z]{1}([a-z]*)((\')?[a-z]*)(\,)?(\s)?)*)$", name)):
        pass
    else:
        print("Назва введена неправильно!")
        return name_validator()
    return name


def reviews_validator():
    reviews = input('Введіть кількість переглядів товару:')
    if bool(re.match('^[1-9]{1}[0-9]*$',reviews)):
        pass
    else:
        print('Неправильно введено кількість переглядів товару')
        return reviews_validator()
    return reviews

def td_validator():
    td = input('Введіть  унікальний номер рядку:')
    if bool(re.match('^([A-Z]*[a-z]*(\_){1,2}(.)*)$',td)):
        pass
    else:
        print('Неправильно введено унікальний номер рядку')
        return td_validator()
    return td