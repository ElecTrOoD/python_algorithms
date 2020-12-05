# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

start = 32
end = 127
line_break = 0

for el in range(start, end + 1):
    print(f'{el}-{chr(el)}\t', end='')
    line_break += 1
    if line_break == 10:
        print()
        line_break = 0

