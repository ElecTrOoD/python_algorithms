# https://drive.google.com/file/d/18krBij4JOlkPAS9ZOno_QCa3wOAzN6lX/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите целое 3-х значное число: '))

c = a % 10
b = a // 10 % 10
a = a // 100

s, e = a + b + c, a * b * c

print(f'сумма: {s}, произведение: {e}')
