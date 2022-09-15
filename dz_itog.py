#!/usr/bin/python3

from random import randrange
import time


def nask(amin=20, amax=1000):
    if amin < 20:
        amin = 20
    if amax > 1000:
        amax = 1000
    assert amin <= amax, 'amin <= amax'
    while True:
        try:
            lsize = int(input(f'Введите размер списка для сортировки от {amin} до {amax}:'))
        except ValueError:
            print('Ошибка! Ожидается ввод числа!')
            continue
        if amin <= lsize <= amax:
            return lsize


def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


# Сформировать список со случайными целыми числами от 10000 до 99999
bs_list = []
for _ in range(nask(10, 100)):
    bs_list.append(randrange(10000, 100000))
# print(f'Unsorted list: {bs_list}')
# Программа должна напечатать:
# - Количество чисел в списке
print(f'Чисел в списке: {len(bs_list)}')
# - Процессорное время, которое было затрачено на сортировку
#   Вывод процессорного времени необходимо напечатать в секундах с точностью 3 знака после запятой.
start = time.time()
bub_sort(bs_list)
end = time.time()
print('Время сортировки пузырьком: %.3f' % (end - start))
# print(f'Sorted list: {bs_list}')
# - Сумму 10 максимальных чисел отсортированного списка
print(f'Сумма 10 максимальных чисел: {sum(bs_list[-10:])}')
# - Сумму 10 минимальных чисел отсортированного списка
print(f'Сумма 10 минимальных чисел: {sum(bs_list[:10])}')
