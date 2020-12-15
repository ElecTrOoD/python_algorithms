import cProfile
import timeit
from math import log, sqrt

import pyexcel


def sieve(n):
    expected_primes = 0
    lst_length = 2
    while expected_primes <= n:
        expected_primes = lst_length / log(lst_length)
        lst_length += 50
    HOLE = 0
    k = 0
    array = [i for i in range(lst_length)]
    array[1] = HOLE

    for i in range(lst_length):
        if array[i] != HOLE:
            prime_num = array[i]
            k += 1
            if k == n:
                return prime_num
            j = i * 2
            while j < lst_length:
                array[j] = HOLE
                j += i


def prime(n):
    prime_num = None
    k = 0
    expected_primes = 0
    lst_length = 2
    while expected_primes <= n:
        expected_primes = lst_length / log(lst_length)
        lst_length += 50
    for dividend in range(2, lst_length):
        if k == n:
            return prime_num
        for divisor in range(2, int(1 + int(sqrt(dividend)))):
            if not dividend % divisor:
                break
        else:
            prime_num = dividend
            k += 1


cProfile.run('sieve(500)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:16(<listcomp>)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:8(sieve)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#        85    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(5000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.026    0.026 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:16(<listcomp>)
#         1    0.023    0.023    0.025    0.025 les_4_task_2.py:8(sieve)
#         1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
#      1092    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(50000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.004    0.004    0.413    0.413 <string>:1(<module>)
#         1    0.029    0.029    0.029    0.029 les_4_task_2.py:16(<listcomp>)
#         1    0.375    0.375    0.409    0.409 les_4_task_2.py:8(sieve)
#         1    0.000    0.000    0.413    0.413 {built-in method builtins.exec}
#     13418    0.004    0.000    0.004    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(500)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.005    0.005    0.005    0.005 les_4_task_2.py:31(prime)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#      3570    0.001    0.000    0.001    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(5000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.118    0.118 <string>:1(<module>)
#         1    0.107    0.107    0.118    0.118 les_4_task_2.py:31(prime)
#         1    0.000    0.000    0.118    0.118 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#     48610    0.011    0.000    0.011    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(50000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.047    4.047 <string>:1(<module>)
#         1    3.875    3.875    4.047    4.047 les_4_task_2.py:31(prime)
#         1    0.000    0.000    4.047    4.047 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#    611952    0.172    0.000    0.172    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


data = [['N', 'T sieve()', 'T prime()']]

for idx in range(10, 1001, 10):
    data.append([idx, timeit.timeit(f'sieve({idx})', number=100, globals=globals()),
                 timeit.timeit(f'prime({idx})', number=100, globals=globals())])

pyexcel.save_as(array=data, dest_file_name="data.xls")

# Вывод. Обе функции имеют линейную зависимость. За счёт класической проверки на делимость функция prime() работает
# ощутимо медленнее.
