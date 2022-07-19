#!/usr/bin/python3

# Конструкции данных

# Задача 1. Дан массив вещественных чисел из 9000 элементов, формируемых с
# помощью датчика случайных чисел. Разбить массив на три части, отсортировать 1 часть
# по убыванию методом пузырька, 2 часть – алгоритмом вставками, 3 часть – алгоритм
# слиянием. Выполнить сравнительный анализ времени работы каждого алгоритма
# сортировок.

import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        lefthalf = arr[:middle]
        righthalf = arr[middle:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1


arr = []
for i in range(9000):
    arr.append(random.uniform(0, 100.0))
arr_1 = arr[:3000]
arr_2 = arr[3000:6000]
arr_3 = arr[6000:]

start = time.time()
bubble_sort(arr_1)
end = time.time()
print(f'Время сортировки пузырьком: {end - start}')

start = time.time()
insert_sort(arr_2)
end = time.time()
print(f'Время сортировки вставками: {end - start}')

start = time.time()
merge_sort(arr_3)
end = time.time()
print(f'Время сортировки слиянием: {end - start}')


# Задача 2. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, имеются ли в массиве три подряд четных числа.

def is_three_even(arr):
    N = len(arr)
    i = 0
    cnt = 0
    while i < N:
        if arr[i] % 2:
            cnt = 0
        else:
            cnt += 1
            if cnt == 3:
                return True
        i += 1
    return False


arr = []
N = 20
for i in range(N):
    arr.append(random.randint(1, 20))
print(arr)
print(is_three_even(arr))


# Задача 3. Даны два стека случайных чисел, размеры стека не более 100 элементов.
# Выполнить объединение стеков в третий стек, располагая элементы в порядке
# убывания. Замечание: при выполнении данной задачи рекомендуется извлечь
# элементы первого стека и второго в общий массив, отсортировать данный массив,
# сформировать третий стек из полученного массива чисел.

def sum_stacks(s1, s2):
    s1len = len(s1)
    s2len = len(s2)
    tmp = []
    for i in range(s1len):
        tmp.append(s1.pop())
    for i in range(s2len):
        tmp.append(s2.pop())
    tmp = sorted(tmp)
    s3 = []
    for i in range(len(tmp)):
        s3.append(tmp.pop())
    return s3


stack_1 = []
stack_2 = []
stack_3 = []
N = 100
for i in range(N):
    stack_1.append(random.randint(1, 50))
    stack_2.append(random.randint(1, 50))
stack_3 = sum_stacks(stack_1, stack_2)
print(stack_3)


# Задача 4. Реализация планировщика очередей. Даны четыре очереди одинаковой длины.
# Значения очередей формируются на основе датчика случайных чисел, границы изменения
# значений 1-10. За один такт обработки очередей – обрабатывается один элемент очереди,
# который имеет наивысший приоритет - максимальное значение из всех очередей. В случае
# равенства приоритетов обрабатывается очередь, которая имеет наибольшую длину. Напечатать
# порядок обслуживания очередей.
# Например, дано
# Очередь 1 - 4 3 2 1
# Очередь 2 - 5 6 7 2
# Очередь 3 - 8 1 4 3
# Очередь 4 - 2 1 5 4
# Порядок обработки: число 4 очередь 4, число 5 очередь 4, число 3 очередь 3, число 4
# очередь 3, число 2 очередь 2, число 7 очередь 2 и т.д.

def proc_queue(deq):
    qlen = []
    used_deqs = []
    for i in range(4):
        qlen.append(len(deq[i]))
        if qlen[i] != 0:
            used_deqs.append(i)
    if len(used_deqs) == 0:
        return True
    last_values = []
    for i in used_deqs:
        last_values.append(deq[i][qlen[i] - 1])
    max_value = max(last_values)
    prior_deqs = []
    for i in used_deqs:
        if deq[i][qlen[i] - 1] == max_value:
            prior_deqs.append(i)
    while len(prior_deqs) > 1:
        if qlen[prior_deqs[0]] < qlen[prior_deqs[1]]:
            prior_deqs.pop(0)
        else:
            prior_deqs.pop(1)
    processed = deq[prior_deqs[0]].pop()
    print(f'В очереди {prior_deqs[0]} обработан элемент {processed}')
    return False


N = 5  # длина очередей
deq = [[0] * N for i in range(4)]
for i in range(4):
    for j in range(N):
        deq[i][j] = random.randint(1, 10)
    print(f'Очередь {i}: {deq[i]}')

is_queue_null = False
while not is_queue_null:
    is_queue_null = proc_queue(deq)
