# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


def hex_addition(first, second):
    summa = deque()
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    k = 0

    if len(first) < len(second):
        first, second = second, first

    for i in range(len(first) - len(second)):
        second.appendleft('0')

    for i in range(len(first) - 1, -1, -1):
        first_term = hex_list.index(first[i])
        second_term = hex_list.index(second[i])
        summa.appendleft(hex_list[(first_term + second_term + k) % 16])
        if first_term + second_term >= 15:
            k = (first_term + second_term + k) // 16
        else:
            k = 0
    if k > 0:
        summa.appendleft(hex_list[k])
    return summa


def hex_factum(first, second):
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    iter_count = 0
    factum_deq = deque()
    for j in range(len(second) - 1, -1, -1):
        second_comp = hex_list.index(second[j])
        factum = deque()
        k = 0

        for i in range(len(first) - 1, -1, -1):
            first_comp = hex_list.index(first[i])
            factum.appendleft(hex_list[(first_comp * second_comp + k) % 16])
            if first_comp * second_comp > 15:
                k = (first_comp * second_comp + k) // 16
            else:
                k = 0
        if k > 0:
            factum.appendleft(hex_list[k])

        for _ in range(iter_count):
            factum.append('0')
        factum_deq.append(factum)
        iter_count += 1
    result = factum_deq[0]
    for i in range(1, len(factum_deq)):
        result = hex_addition(result, factum_deq[i])
    return result


a = deque(input('Введите первое шестнадцатеричное число: ').upper())
b = deque(input('Введите второе шестнадцатеричное число: ').upper())

print(f'Произведение шестнадцатеричных чисел {"".join(a)} и {"".join(b)} равно {"".join(hex_factum(a, b))}')
print(f'Сумма шестнадцатеричных чисел {"".join(a)} и {"".join(b)} равна {"".join(hex_addition(a, b))}')
