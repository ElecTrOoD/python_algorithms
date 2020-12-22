# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
from random import randint

Enterprise = namedtuple('Enterprise', ['first_quart', 'second_quart', 'third_quart', 'fourth_quart'],
                        defaults=[0, 0, 0, 0])
enterprise_dict = {}

ent_quantity = int(input('Введите количество предприятий: '))
for i in range(ent_quantity):
    name = input(f'Название {i + 1}-го предприятия: ')
    enterprise_dict[name] = Enterprise(
        randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
        # int(input('Прибыль за 1-й квартал: ')),
        # int(input('Прибыль за 2-й квартал: ')),
        # int(input('Прибыль за 3-й квартал: ')),
        # int(input('Прибыль за 4-й квартал: '))
    )

profit_list = []
for key, val in enterprise_dict.items():
    print(f'{key} — прибыль за год: {sum(val)}')
    profit_list += val

avg_profit_list = sum(profit_list) / len(enterprise_dict)
print(f'Средняя прибыль всех предприятий за год: {avg_profit_list}')

print('Предприятия с прибылью выше среднего:')
for key, val in enterprise_dict.items():
    if sum(val) > avg_profit_list:
        print(f'{key} - {sum(val)}')

print('Предприятия с прибылью ниже среднего:')
for key, val in enterprise_dict.items():
    if sum(val) < avg_profit_list:
        print(f'{key} - {sum(val)}')
