# Побудувати рекурсивну функцію, що друкує кількісь ключив за умови, що назва ключа більш трійки

i = 0
def recursion(dataset, i):
    N = list(dataset.keys())
    if len(dataset) > i:
        if len(N[i]) > 3:
            return recursion(dataset, i-1) + dataset[N[i]].get('name')
    else:
        return 0

print(recursion(dataset, i))