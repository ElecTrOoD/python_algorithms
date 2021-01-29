# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите натуральное число: '))

el = 1
summa = 0
for _ in range(n):
    summa += el
    el /= -2

print(f'Сумма элементов последовательности: {summa}')