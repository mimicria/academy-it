#!/usr/bin/python3

# Вложенные циклы, двумерные списки

# Задача 1. Написать программу для вывода узора по образцу, используя вложенный цикл.
N = 9
rev = 0
for i in range(N):
    rev += i // ((N + 1) // 2) * 2
    for j in range(i + 1 - rev):
        print('*', end='')
    print()

# Задача 2. Совершенным числом называется целое положительное число, равное сумме
# своих положительных делителей, исключая само число. Например, 6 имеет делители 1, 2 и
# 3 (исключая само себя), а 1 + 2 + 3 = 6, поэтому 6 — совершенное число.
# Напишите программу, которая выводит все совершенные числа от 1 до 100
for i in range(1, 101):
    sum = 0
    for j in range(1, i // 2 + 1):
        if not i % j:
            sum += j
    if sum == i:
        print(i)

# Задача 1 "Снежинка"
# Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив
# его символами "."(каждый элемент массива является строкой из одного символа).
# Затем заполните символами "*" среднюю строку массива, средний столбец массива,
# главную диагональ и побочную диагональ. В результате единицы в массиве должны
# образовывать изображение звездочки. Выведите полученный массив на экран,
# разделяя элементы массива пробелами.
n = 7
A = [['.'] * n for i in range(n)]
for i in range(n):
    A[i][i] = '*'
    A[n // 2][i] = '*'
    A[i][n // 2] = '*'
    A[i][n - i - 1] = '*'

for row in A:
    for elem in row:
        print(elem, end=' ')
    print()

print('\n')
# Задача 2 "Шахматная доска" Даны два числа n и m. Создайте двумерный массив
# размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом
# верхнем углу должна стоять точка.

n = 7
m = 8
A = [['.'] * m for i in range(n)]
for i in range(m):
    for j in range(n):
        if (i + j) % 2: A[j][i] = '*'

for row in A:
    for elem in row:
        print(elem, end=' ')
    print()


# Задача 3 "Поменять столбцы" Дан двумерный массив и два числа: i и j. Поменяйте
# в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива,
# затем числа i и j. Решение оформите в виде функции swap_columns(a, i, j)
def swap_columns(a, i, j):
    for x in range(len(a)):
        a[x][j], a[x][i] = a[x][i], a[x][j]


A = [[1, 2, 3, 4, 5] for i in range(5)]
swap_columns(A, 1, 3)

for row in A:
    for elem in row:
        print(elem, end=' ')
    print()

# Задание для закрепления темы: Дан список чисел. Используя функцию enumerate()
# в заголовке цикла for, создайте второй список, в котором каждый элемент должен быть
# строкой, включающей через пробел индекс и значение соответствующего элемента
# первого списка.
A = [1, 2, 3, 4, 5, 6]
B = []
for i in enumerate(A):
    B.append(' '.join(map(str, i)))
print(B)
