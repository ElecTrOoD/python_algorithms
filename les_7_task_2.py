# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform

START = 0
END = 50 - 1
LENGTH = 10


def sort_func(arr):
    def sort_list(left_list, right_list):
        sorted_list = []
        i = j = 0
        left_length, right_length = len(left_list), len(right_list)

        for _ in range(left_length + right_length):
            if i < left_length and j < right_length:
                if left_list[i] <= right_list[j]:
                    sorted_list.append(left_list[i])
                    i += 1
                else:
                    sorted_list.append(right_list[j])
                    j += 1
            elif i == left_length:
                sorted_list.append(right_list[j])
                j += 1
            elif j == right_length:
                sorted_list.append(left_list[i])
                i += 1
        return sorted_list

    if len(arr) <= 1:
        return arr

    left_half, right_half = sort_func(arr[:len(arr) // 2]), sort_func(arr[len(arr) // 2:])
    return sort_list(left_half, right_half)


array = [uniform(START, END) for _ in range(LENGTH)]
print(array)
z = sort_func(array)
print(z)
