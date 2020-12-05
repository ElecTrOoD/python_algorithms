# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.


from random import randint

attempts = 10
num = randint(0, 100)
print("Загадано случайное число от 0 до 100, попытайтесь его угадать. У вас 10 попыток!")

for i in range(1, attempts + 1):
    answer = int(input('Введите целое число от 0 до 100: '))
    if answer < num:
        print(f'Число больше, у вас осталось {attempts - i} '
              f'{"попытки!" if 5 > attempts - i > 1 else "попытка!" if attempts - i == 1 else "попыток!"}')
    elif answer > num:
        print(f'Число меньше, у вас осталось {attempts - i} '
              f'{"попытки!" if 5 > attempts - i > 1 else "попытка!" if attempts - i == 1 else "попыток!"}')
    else:
        print(f'Верно! Вы угадали с {i} попытки.')
        break
else:
    print(f'Вы не смогли угадать число за отведенное число попыток. Правильный ответ: {num}')
