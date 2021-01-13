# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# После исполнения скрипт занимает 1421 байт. Время исполнения 0.0223872 (numbers=1000).

from sys import getsizeof

array = [3, 0, 1, 2, 0, 1, 7, 6, 6, 7, 1, 7, 2, 1, 6, 3, 4, 7, 7, 5, 3, 5, 3, 3, 0, 7, 2, 4, 3, 5]

max_list = [[], 1]
for comp_1 in array:
    occurred = 0
    for comp_2 in array:
        if comp_1 == comp_2:
            occurred += 1
    if max_list[1] < occurred:
        max_list[1] = occurred
for item in set(array):
    if array.count(item) == max_list[1]:
        max_list[0].append(item)
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
