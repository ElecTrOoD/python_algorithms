# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
d = {'max_item': array[0], 'max_pos': 0, 'min_item': array[0], 'min_pos': 0}

# Так как значение первого элемента уже записано в max_el и min_el, не имеет смысла проверять его.
# Но срез создаёт копию массива, расходуя драгоценную память.
# Как лучше сделать в этой ситуации, провести бессмысленную проверку или сделать копию объекта?
for pos, item in enumerate(array[1:], 1):
    if item > d['max_item']:
        d['max_item'], d['max_pos'] = item, pos
    elif item < d['min_item']:
        d['min_item'], d['min_pos'] = item, pos

print(array)
print(d)

array[d['min_pos']], array[d['max_pos']] = d['max_item'], d['min_item']

print(array)
