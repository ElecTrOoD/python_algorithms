# Определить, какое число в массиве встречается чаще всего.

from random import randint


def get_key(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    return keys


SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 7

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
d = {}
max_ = 1

for el in array:
    d[el] = 0
    for item in array:
        if item == el:
            d[el] += 1
    if d[el] > max_:
        max_ = d[el]

max_keys = get_key(d, max_)

print(array)
print(d)
print()
print(f'{max_} раза' if 5 > max_ > 2 else f'{max_} раз', end=' ')
print(f'встречается цифра ' if len(max_keys) == 1 else f'встречаются цифры ', end='')
print(*max_keys, sep=', ')
