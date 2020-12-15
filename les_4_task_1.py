# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
#
# Мне понравилась идея с гугл таблицей, решил тоже попробовать реализовать.
# https://docs.google.com/spreadsheets/d/1RS8HhUbBHw_z1RvWZyI8Yg942GkpIAi1EHzAD__4hpc/edit?usp=sharing

import cProfile
from random import randint
from timeit import timeit

import pyexcel


def reverse_rec(num):
    if num < 10:
        return num
    number_signs = 0
    temp = num
    res = num % 10
    num //= 10
    while temp >= 10:
        temp //= 10
        number_signs += 1
    return res * 10 ** number_signs + reverse_rec(num)


def reverse_lst(num):
    num = list(str(num))
    length = len(num)
    for i in range((length // 2)):
        num[i], num[length - i - 1] = num[length - i - 1], num[i]
    num = int("".join([i for i in num]))
    return num


def reverse_slice(num):
    num = str(num)
    num = num[::-1]
    return int(num)


data = [['N', 'T reverse_rec()', 'T reverse_lst()', 'T reverse_slice()']]
test_number_main = str(randint(10 ** (500 - 1), 10 ** 500 - 1))
test__rec_number_small = randint(10 ** (10 - 1), 10 ** 10 - 1)
test__rec_number_med = randint(10 ** (100 - 1), 10 ** 100 - 1)
test__rec_number_big = randint(10 ** (990 - 1), 10 ** 990 - 1)
test_number_small = randint(10 ** (500 - 1), 10 ** 500 - 1)
test_number_med = randint(10 ** (5000 - 1), 10 ** 5000 - 1)
test_number_big = randint(10 ** (50000 - 1), 10 ** 50000 - 1)

cProfile.run(f'reverse_rec({test__rec_number_small})')  # n = 10**10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 les_4_task_1.py:13(reverse_rec)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run(f'reverse_rec({test__rec_number_med})')  # n = 10**100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     100/1    0.001    0.000    0.001    0.001 les_4_task_1.py:16(reverse_rec)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run(f'reverse_rec({test__rec_number_big})')  # n = 10**990
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.435    0.435 <string>:1(<module>)
#     990/1    0.435    0.000    0.435    0.435 les_4_task_1.py:16(reverse_rec)
#         1    0.000    0.000    0.435    0.435 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run(f'reverse_lst({test_number_small})')  # n = 10**500
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:29(reverse_lst)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:34(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run(f'reverse_lst({test_number_med})')  # n = 10**5000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 les_4_task_1.py:29(reverse_lst)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:34(<listcomp>)
#         1    0.001    0.001    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run(f'reverse_lst({test_number_big})')  # n = 10**50000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.251    0.251 <string>:1(<module>)
#         1    0.249    0.249    0.251    0.251 les_4_task_1.py:29(reverse_lst)
#         1    0.001    0.001    0.001    0.001 les_4_task_1.py:34(<listcomp>)
#         1    0.057    0.057    0.308    0.308 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.001    0.001    0.001    0.001 {method 'join' of 'str' objects}


cProfile.run(f'reverse_slice({test_number_small})')  # n = 10**500
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:38(reverse_slice)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run(f'reverse_slice({test_number_med})')  # n = 10**5000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les_4_task_1.py:38(reverse_slice)
#         1    0.001    0.001    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run(f'reverse_slice({test_number_big})')  # n = 10**50000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.230    0.230 <string>:1(<module>)
#         1    0.230    0.230    0.230    0.230 les_4_task_1.py:38(reverse_slice)
#         1    0.056    0.056    0.286    0.286 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


for idx in range(5, 501, 5):
    n = int(test_number_main[:idx])
    data.append([idx, timeit(f'reverse_rec({n})', number=100, globals=globals()),
                 timeit(f'reverse_lst({n})', number=100, globals=globals()),
                 timeit(f'reverse_slice({n})', number=100, globals=globals())])

pyexcel.save_as(array=data, dest_file_name="data_2.xls")

# Вывод. Рекурсивная функция переворота числа reverse_rec() имеет квадратичную зависимость времени испольнения от
# количества разрядов числа N. Оставшиеся две функции имеют линейную зависимость. Самой удачной считаю reverse_slice().
# Эта функция превосходит остальные как по времени исполнения, так и, скорее всего, по потреблению оперативной
# памяти. Сам код функции максимально простой и понятный.
