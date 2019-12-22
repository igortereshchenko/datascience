from snitsarenkoas.validator.lib import id_validator
from snitsarenkoas.validator.lib import name_validator
from snitsarenkoas.validator.lib import reviews_validator
from snitsarenkoas.validator.lib import upc_validator

id=id_validator(input('Введіть індивідуальну назву:'))
name=name_validator(input('Введіть назву взуття: '))
reviews=reviews_validator(input('Введіть відгук:'))
upc=upc_validator(input(('Введіть індивідуальний код:')))