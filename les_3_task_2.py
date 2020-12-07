# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
# 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих
# позициях первого массива стоят четные числа.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
new_array = []

for pos, item in enumerate(array):
    if item % 2 == 0:
        new_array.append(pos)

print(array)
print(new_array)
