# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

SIZE_N = 5
SIZE_M = 4
matrix = []

for i in range(SIZE_N):
    matrix.append([])
    line_sum = 0
    for j in range(SIZE_M - 1):
        matrix[i].append(int(input()))
        line_sum += matrix[i][j]
    matrix[i].append(line_sum)

for line in matrix:
    for el in line:
        print(f'{el:>4}\t', end='')
    print()
