# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

from random import randint

START = -100
END = 100 - 1
LENGTH = 10


def sort_func(arr):
    comp = True
    while comp:
        comp = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                comp = True


array = [randint(START, END) for _ in range(LENGTH)]
print(array)
sort_func(array)
print(array)
