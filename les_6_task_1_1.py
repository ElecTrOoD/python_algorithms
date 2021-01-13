# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти. В диапазоне
# натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. После
# исполнения скрипт занимает 2165 байт. Время исполнения 0.0387563 (numbers=1000).
#
# Вывод для всех 3-ех вариантов решения задачи. В данной задаче списки явно выигрывают по количеству потребляемой памяти
# перед словарями, не теряя в информативности (решение No2). Использование коллекции Counter увеличивает потребление
# памяти (~ на 20%), но даёт выигрыш в производительности ~ в 5 раз. Оптимальным решением данной задачи считаю
# способ No3. Отличная производительность, хорошая эффективность потребления памяти, наименьшее количество строк кода.
#
# Windows 10 x64
# x64 Python 3.9.1 x64

from sys import getsizeof
from random import randint


def get_key(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    return keys


# SIZE = 30
# MIN_ITEM = 0
# MAX_ITEM = 7
#
# array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array = [3, 0, 1, 2, 0, 1, 7, 6, 6, 7, 1, 7, 2, 1, 6, 3, 4, 7, 7, 5, 3, 5, 3, 3, 0, 7, 2, 4, 3, 5]
d = {}
max_ = 1

for el in array:
    if str(el) in list(d.keys()):
        continue
    d[el] = 0
    for item in array:
        if item == el:
            d[el] += 1
    if d[el] > max_:
        max_ = d[el]

max_keys = get_key(d, max_)
print(d)


exceptions = ['exceptions', 'val_lst', 'function', 'builtin_function_or_method', 'method']
val_lst = []
for item in dir():
    if not item.startswith('_') and item not in exceptions:
        type_ = str(eval('type(' + item + ')')).replace('<class \'', '').replace('\'>', '')
        if type_ in exceptions:
            continue
        value = eval(f'{type_}({item})')
        if value not in val_lst:
            val_lst.append(value)

mem_sum = 0
for item in val_lst:
    if hasattr(item, '__iter__'):
        if hasattr(item, 'items'):
            for key, val in item.items():
                mem_sum += getsizeof(key) + getsizeof(val)
        elif type(item) != str:
            for value in item:
                mem_sum += getsizeof(value)
    mem_sum += getsizeof(item)

print(mem_sum)
