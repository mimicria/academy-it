#!/usr/bin/python3

# Списки

# Задание 1 . Допишите код, чтобы вывести последний элемент списка
# данный код
sample = ["abc", "xyz", "aba", 1221]
# требуемый вывод:
# 1221
print(sample[-1])

# Задание 2 . Допишите код, чтобы вывести расширенный список
# данный код
sample = ["Green", "White", "Black"]
print(sample)
# требуемый вывод:
# ["Red", "Green", "White", "Black", "Pink", "Yellow"]
sample.insert(0,"Red")
sample+="Pink", "Yellow"
print(sample)

# Задание 3. Написать программу: дан список из 10 чисел, которые задаются с помощью
# датчика случайных чисел. Программа находит повторяющиеся элементы и считает
# количество повторений. Например дан список (1,1,1,2,3,4,2,3,4) результат число 1
# повторяется 3 раза, число 2 – 2раза, число 3 - 2 раза, число 4 – 2 раза
from random import randrange
spisok = []
for i in range(10):
    spisok.append(randrange(5))
print (spisok)
uniq = set(spisok)
for i in uniq:
    print("Число", i, "повторяется", spisok.count(i), "раза")

# Задание 4 . Написать программу: дан список из 10 чисел, которые задаются с помощью
# датчика случайных чисел. Программа находит повторяющиеся элементы и удаляет их из
# списка. Например дан список (1,1,1,2,3,4,2,3,4) результат (1,2,3,4)
from random import randrange
spisok = []
for i in range(10):
    spisok.append(randrange(5))
print (spisok)
print (list(set(spisok)))

# Задание 5. Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно
# присутствует, замените его на 200. Обновите список только при первом вхождении числа 20.
spisok = [2, 3, 4, 5, 20, 11, 12, 20, 15]
if spisok.count(20)>0:
    spisok[spisok.index(20)]=200
print(spisok)

# Задание 6. Поменять местами самый большой и самый маленький элементы списка
spisok = [2, 1, 4, 5, 20, 11, 12, 21, 15]
i_max = spisok.index(max(spisok))
i_min = spisok.index(min(spisok))
spisok[i_max], spisok[i_min] = spisok[i_min], spisok[i_max]
print(spisok)

# Кортежи

# 1. Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму.
# данный код
numbers = (0,1,2,3,4,5,6,7,8,9)
print(sum(numbers))
# требуемый вывод:
# 45

# 2. Введите статистику частотности букв в кортеже.
# - решение 1- использование циклов
# - решение 2 – использование встроенных функций
# данный код
long_word = (
'т', 'т', 'а', 'и', 'и', 'а', 'и',
'и', 'и', 'т', 'т', 'а', 'и', 'и',
'и', 'и', 'и', 'т', 'и'
)
# требуемый вывод:
# Количество 'т': 5
# Количество 'а': 3
# Количество 'и': 11

# решение 1
count_t=count_a=count_i=0
for i in long_word:
    if i=='т':
        count_t+=1
    elif i=='а':
        count_a += 1
    elif i == 'и':
        count_i += 1
print("Количество 'т':", count_t)
print("Количество 'a':", count_a)
print("Количество 'и':", count_i)
# решение 2
print("Количество 'т':", long_word.count('т'))
print("Количество 'a':", long_word.count('а'))
print("Количество 'и':", long_word.count('и'))

# Словари

# Задание 1. Выведите значение возраста из словаря person.
# данный код
person = {"name": "Kelly", "age":25, "city": "New york"}
# требуемый вывод:
# 25
print(person["age"])

# Задание 2. Значениями словаря могут быть и списки. Допишите словарь с
# ключами BMW, ВАЗ, Tesla и списками из 3х моделей в качестве значений.
# данный код
models_data = {"BMW": ["X1","X3","X6"],
               "Tesla": ["Modes S","Model X", "Cybertruck"],
               "ВАЗ": ["2101","2108","Калина"]
}
print(models_data["Tesla"][0])
# требуемый вывод:
# Modes S

# Задание 3. Дан список из 10 чисел, которые задаются случайном образом.
# Сформировать словарь по следующему принципу: ключ (one, two, three):элемент списка
# Задача подсчитать количество повторений значений. Пример значение 2 –
# встречается дважды.
# models_data = {“one”:1, “two”:2, “tree”:2, “four”:3…}
from random import randrange
keys = ["one","two","three","four","five","six","seven","eight","nine","ten"]
models_data = {key: randrange(5) for key in keys}
print(models_data)
val=list(models_data.values())
uniq = set(val)
for i in uniq:
    rep=val.count(i)
    if rep>1:
        print("Значение", i, "встречается", rep, "раза")

# Задание 4. Даны два списка одинаковой длины. Необходимо создать из них
# словарь таким образом, чтобы элементы первого списка были ключами, а
# элементы второго — соответственно значениями нашего словаря.
keys = ["one","two","three","four"]
items = [1,2,3,4]
models_data = dict(zip(keys,items))
print(models_data)

# Задание 5. Дан словарь с числовыми значениями. Необходимо их все
# перемножить и вывести на экран.
# !!! Взял словарь из задания 4, он с числовыми значениями как раз
val=list(models_data.values())
res=1
for i in val:
    res*=i
print(res)

# Задание 6. Создайте словарь из строки 'pythonist' следующим образом: в
# качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
str='pythonist'
spisok = list(str)
res = dict.fromkeys(spisok)
for i in res:
    res[i]=spisok.count(i)
print(res)

