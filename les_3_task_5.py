# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

SIZE = 20
MIN_ITEM = -50
MAX_ITEM = 50

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_neg = 0
neg_el_found = False

for item in array:
    if max_neg == -1:
        break
    elif item < 0 and neg_el_found is False:
        max_neg = item
        neg_el_found = True
    elif 0 > item > max_neg:
        max_neg = item

print(array)
print(max_neg)
