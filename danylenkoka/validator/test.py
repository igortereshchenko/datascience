from danylenkoka.validator.lib import *

# Тестим год

print(cen_year_validator('2005')) # Возвращает True
print(cen_year_validator('222')) # озвращает False

# Тестим наличие проводов и стен (валидаторы там одинаковые)

print(wire_2nd_validator('yEs')) # Возвращает True
print(vert_wall_validator('Коля')) # Возвращает False

# Тестим расположение деревьев

print(tree_loc_validator('Front')) # Возвращает True
print(tree_loc_validator('Kiev')) # Возвращает False