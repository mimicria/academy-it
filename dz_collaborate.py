#!/usr/bin/python3

# Командная работа

# Задание: Реализовать набор методов реализующие работу с массивами целых чисел.
# Описание реализуемых методов представлена ниже:

# - Инициализация массива на основе датчика случайных чисел – Create_random - два
# аргумента функции – массив, размер массива
from random import randrange


def Create_random(arr: list, arr_size: int):
    assert type(arr_size) is int, 'Размер массива должен быть числом'
    assert type(arr) is list, 'В качестве массива ожидается список'
    assert arr_size > 0, 'Размер массива должен быть целым положительным числом'
    arr.clear()
    for i in range(arr_size):
        arr.append(randrange(100))


# - Инициализация массива с помощью пользователя числе – Create_manual - два аргумента
# функции – массив, размер массива. Значение элементов массива осуществляется пользователем
def Create_manual(arr: list, arr_size: int):
    assert type(arr_size) is int, 'Размер массива должен быть числом'
    assert type(arr) is list, 'В качестве массива ожидается список'
    assert arr_size > 0, 'Размер массива должен быть целым положительным числом'
    arr.clear()
    i = 0
    while i < arr_size:
        try:
            arr.append(int(input(f'Введите {i + 1} элемент массива: ')))
        except ValueError:
            print('Ошибка! Ожидается ввод числа!')
            continue
        i += 1


# - * (выполняется по желанию) Инициализация массива путем считывания файла.–
# Create_from_file - два аргумента функции – файл чтения, размер массива.


# - Печать массива – Print_array – один аргумент функции – массив – вывести на экран
# значения массива
def Print_array(arr: list):
    assert type(arr) is list, 'В качестве массива ожидается список'
    print(*arr)


# - Поиск заданного элемента Find_value– два аргумента функции – массив, искомый
# элемент – функция возвращает все номера индексов где встречается искомый элемент
def Find_value(arr: list, val: int) -> list:
    assert type(arr) is list, 'В качестве массива ожидается список'
    assert type(val) is int, 'Искомый элемент должен быть числом'
    res = []
    for i in range(len(arr)):
        if arr[i] == val:
            res.append(i)
    return res


# - Удаление заданного элемента Delete_value– два аргумента функции – массив, искомый
# элемент – функция возвращает массив, в котором удалены все значения искомого элемента
def Delete_value(arr: list, val: int) -> list:
    assert type(arr) is list, 'В качестве массива ожидается список'
    assert type(val) is int, 'Искомый элемент должен быть числом'
    res = []
    for i in arr:
        if i != val:
            res.append(i)
    return res


# - Подсчет среднего арифметического элементов массива Everage один аргумент функции –
# массив –функция возвращает среднее арифметическое элементов массива
def Everage(arr: list) -> float:
    assert type(arr) is list, 'В качестве массива ожидается список'
    if len(arr) == 0:
        return 0
    summ = 0
    for i in arr:
        try:
            summ += int(i)
        except ValueError:
            print('Ошибка! В массиве содержатся не только числа!')
            return -1
    return summ / len(arr)


# - Сложение массивов Sum_array два аргумента функции – массив_1, массив_2, сложение
# возможно при равенстве длин массивов, сложение выполняет поэлементо, функция
# возвращает массив сумм элементов массива1+массива_2
def Sum_array(arr1: list, arr2: list) -> list:
    assert type(arr1) is list, 'В качестве 1 массива ожидается список'
    assert type(arr2) is list, 'В качестве 2 массива ожидается список'
    if len(arr1) != len(arr2):
        print('Ошибка! Массивы разной длины!')
        return []
    res = []
    for i in range(len(arr1)):
        try:
            res.append(int(arr1[i]+arr2[i]))
        except ValueError:
            print('Ошибка! В массиве содержатся не только числа!')
            return []
    return res
