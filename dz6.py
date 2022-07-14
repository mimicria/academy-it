#!/usr/bin/python3

# Массивы

import array

# Задача 1. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, имеются ли в массиве два подряд числа с разницей значений между ними 1.

a = array.array('i',[1,3,6,4,7,8,11])
N = len(a)
razn = False
for i in range(N-1):
    if abs(a[i]-a[i+1])==1:
        razn = True
        break
if razn:
    print('Yes')
else:
    print('No')

# Задача 2. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Вместо каждого элемента с нулевым значением поставить сумму двух предыдущих
# элементов массива.

a = array.array('i',[1,3,6,0,7,8,11])
N = len(a)
for i in range(N):
    if a[i]==0:
        a[i]=a[i-1]+a[i-2]
print (a)

# Задача 3. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Вставить группу из M новых элементов, начиная с позиции K.

a = array.array('i',[1,3,6,0,7,8,11])
N = len(a)
K = 2
M = 3
for i in range(M):
    print(f"Введите добавляемое число {i+1}:")
    a.insert(K+i,int(input()))
print (a)

# Задача 4. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Поменять местами первую и вторую половины массива без использования
# дополнительных массивов

a = array.array('i',[1,3,6,0,7,8,11])
N = len(a)
pol = int(N/2)
nr = 0
if N%2:
    nr = 1
for i in range(pol):
    a[i],a[pol+i+nr] = a[pol+i+nr],a[i]
print(a)

# Задача 5. Реализовать проект – операций над массивами, каждая подзадача
# реализуется в виде отдельной функции:

# - инициализация массива с помощью датчика случайных чисел. Размер массива
# определяет пользователь
import random

def arr_init(arr,N):
    for i in range(N):
        arr.append(random.randrange(15))

a = array.array('i')
N=3
arr_init(a,N)
print(a)

# - сложение массивов поэлементно в случае равенства длины массивов
def arr_sum(arr1,arr2):
    if len(arr1)==len(arr2):
        ret = array.array('i')
        for i in range(len(arr1)):
            ret.append(arr1[i]+arr2[i])
        return ret
a = array.array('i',[1,1,1])
b = array.array('i',[2,2,2])
c = arr_sum(a,b)
print(c)

# - умножение массива на число осуществляется поэлементно
def arr_mul(arr,num):
    ret = array.array('i')
    for i in range(len(arr)):
        ret.append(arr[i]*num)
    return ret

a = array.array('i', [1, 2, 3])
b = arr_mul(a,3)
print(b)

# - поиск общих значений двух массивов (длина массивов может быть разная)
def arr_comp(arr1,arr2):
    ret = array.array('i')
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                ret.append(arr1[i])
                break
    return ret

a = array.array('i',[1,2,3,4])
b = array.array('i',[3,4,5,6])
c = arr_comp(a,b)
print(c)

# - печать значений массива
def arr_prnt(arr):
    for i in range(len(arr)):
        print(arr[i])

a = array.array('i',[1,2,3,4])
arr_prnt(a)

# - упорядочивание значений массива по убыванию (без использования стандартных функций)
def arr_descsort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

a = array.array('i',[1,2,4,3])
arr_descsort(a)
print(a)

# - поиск min, max значений в массиве, среднего значения (без использования стандартных функций)
def arr_stat(arr):
    n = len(arr)
    if not n:
        print('Массив пустой')
        return None
    stat = {"min": arr[0], "max": arr[0], "avg": 0.0}
    sum=0
    for i in range(n):
        sum+=arr[i]
        if arr[i]>stat["max"]:
            stat["max"]=arr[i]
        if arr[i]<stat["min"]:
            stat["min"] = arr[i]
    stat["avg"]=sum/n
    return stat

a = array.array('i', [1, 2, 4, 3, 9])
print(a)
res = arr_stat(a)
if res is not None:
    print(f'Min: {res["min"]}, Max: {res["max"]}, Avg: {res["avg"]}')