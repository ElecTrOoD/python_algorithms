# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# После исполнения скрипт занимает 1716 байт. Время исполнения 0.0043275(numbers=1000).

from sys import getsizeof
from collections import Counter

array = [3, 0, 1, 2, 0, 1, 7, 6, 6, 7, 1, 7, 2, 1, 6, 3, 4, 7, 7, 5, 3, 5, 3, 3, 0, 7, 2, 4, 3, 5]
max_list = Counter(array).most_common()

while max_list[0][1] != max_list[-1][1]:
    max_list.remove(max_list[-1])
print(max_list)

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
