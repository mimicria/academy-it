#!/usr/bin/python3

# Даны два списка чисел. Реализовать для списков чисел операции – поиск максимального
# элемента, поиск заданного элемента и указания позиций нахождения в списке, удаление
# заданного элемента, печать элементов списке, сложение списков поэлементно при равной
# длине списков. Написать программу реализации данной задачи, с учетом следующих требований:

# - заполнение списка осуществляется на основе датчика случайных чисел, и реализация
# осуществляется в виде функции, которой в качестве аргумента указывается размер списка
from random import randrange


def random_list(arr: list, arr_size: int):
    assert type(arr_size) is int, 'Размер списка должен быть числом'
    assert type(arr) is list, 'Аргументом ожидается список'
    assert arr_size > 0, 'Размер списка должен быть целым положительным числом'
    arr.clear()
    for i in range(arr_size):
        arr.append(randrange(10))


# - реализация печати элементов списка осуществляется в виде функции, которой в качестве
# аргумента указывается список чисел
def print_list(arr: list):
    assert type(arr) is list, 'Аргументом ожидается список'
    print(*arr)


# - реализация поиска заданного элемента списка осуществляется в виде функции, которой в
# качестве аргумента указывается список чисел, и искомое число. Функция возвращает
# результат – номер позиции где впервые найден данный элемент
def find_value(arr: list, val: int) -> int:
    assert type(arr) is list, 'Аргументом ожидается список'
    assert type(val) is int, 'Искомый элемент должен быть числом'
    if val in arr:
        return arr.index(val)


# - реализация поиска заданного элемента с указанием всех позиций нахождения в списке
# осуществляется в виде функции, которой в качестве аргумента указывается список чисел, и
# искомое число. Функция возвращает результат – список номеров позиций где найден данный
# элемент
def find_values(arr: list, val: int) -> list:
    assert type(arr) is list, 'Аргументом ожидается список'
    assert type(val) is int, 'Искомый элемент должен быть числом'
    res = []
    for i in range(len(arr)):
        if arr[i] == val:
            res.append(i)
    return res


# - реализация удаление заданного элемента в списке осуществляется в виде функции, которой
# в качестве аргумента указывается список чисел, и искомое число. Функция возвращает
# результат – список без указанного элемента
def delete_values(arr: list, val: int) -> list:
    assert type(arr) is list, 'Аргументом ожидается список'
    assert type(val) is int, 'Искомый элемент должен быть числом'
    res = []
    for i in arr:
        if i != val:
            res.append(i)
    return res


# - реализация сложения списков чисел осуществляется в виде функции, которой в качестве
# аргумента указывается списки чисел. Функция возвращает результат – печать на экране
# сообщения «сложение невозможно, из-за несовпадения длин списков», или список, в котором
# выполнено сложение поэлементно двух заданных списков чисел
def sum_lists(arr1: list, arr2: list) -> list:
    assert type(arr1) is list, 'Аргументом 1 ожидается список'
    assert type(arr2) is list, 'Аргументом 2 ожидается список'
    if len(arr1) != len(arr2):
        print('Сложение невозможно из-за несовпадения длин списков')
        return []
    res = []
    for i in range(len(arr1)):
        try:
            res.append(int(arr1[i] + arr2[i]))
        except ValueError:
            print('Ошибка! В массиве содержатся не только числа!')
            return []
    return res


# - размер списка числе определяется пользователем программы. Выполнить контроль ввода
# информации – число должно быть положительное и не более 20

while True:
    try:
        length = int(input('Введите размер списка:'))
    except ValueError:
        print('Ошибка, ожидается число!')
        continue
    else:
        if 0 < length < 20:
            break
        else:
            print('Ожидается положительное число не более 20')
            continue
a = []
b = []
random_list(a, length)
random_list(b, length)
print_list(a)
print_list(b)
print(find_value(a, 5))
print(find_values(a, 5))
print(delete_values(a, 5))
print(sum_lists(a, b))
