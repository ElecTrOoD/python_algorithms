# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

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


a = int(input('Введите натуральное число: '))
rev_a = reverse_rec(a)

print(rev_a)
