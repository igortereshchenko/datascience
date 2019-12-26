import lib as validate

host_location = input('Введите Ваш город проживания на англ.\n')
print("Верно." if validate.host_location_validator(host_location) else "Не верно.")

host_is_superhost = input('Если Вы мега-арендадатель, напишите 1, если нет - 0\n')
print("Верно." if validate.host_is_superhost_validator(bool(host_is_superhost)) else "Не верно.")

street = input('Введите адрес объекта\n')
print("Верно." if validate.street_validator(int(street)) else "Не верно.")

host_name = input('Введите Ваше имя\n')
print("Верно." if validate.host_name_validator(int(host_name)) else "Не верно.")