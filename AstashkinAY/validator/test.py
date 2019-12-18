import lib as validate

name = input('Введите дату в формате YYYY-MM-DD\n')
print("Верно." if validate.name_validator(name) else "Не верно.")

host_name = input('Если Вы мега-арендадатель, напишите 1, если нет - 0\n')
print("Верно." if validate.host_name_validator(host_name) else "Не верно.")

host_since = input('Введите адрес объекта\n')
print("Верно." if validate.host_since_validator(host_since) else "Не верно.")
