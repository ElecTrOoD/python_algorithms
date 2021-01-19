# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

from random import choice, randint

M = 25
START = -(M ** 2)
END = M ** 2
LENGTH = M * 2 + 1


def find_median(arr, k=None):
    if len(arr) == 1:
        return arr[0]
    if k is None:
        k = len(arr) // 2

    pivot = choice(arr)
    less = [i for i in arr if i < pivot]
    more = [i for i in arr if i > pivot]
    pivots = [i for i in arr if i == pivot]
    length_less = len(less)
    length_pivots = len(pivots)

    if k < length_less:
        return find_median(less, k)
    elif k < length_less + length_pivots:
        return pivots[0]
    else:
        return find_median(more, k - length_less - length_pivots)


array = [randint(START, END) for _ in range(LENGTH)]
print(find_median(array))

# Проверка
s_array = sorted(array)
print(s_array[len(array) // 2])
