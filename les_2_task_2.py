# https://drive.google.com/file/d/16BrlHOnD1nf8L708RxArsRegOtu2FL7P/view?usp=sharing
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите натуральное число: '))
even = 0
odd = 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10

print(f'Количество чётных цифр введенного числа: {even}, нечётных: {odd}')
