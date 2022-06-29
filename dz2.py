#!/usr/bin/python3

# Списки

# Задание 1 . Допишите код, что бы вывести последний элемент списка
# данный код
sample = ["abc", "xyz", "aba", 1221]
# требуемый вывод:
# 1221
print(sample[-1])

# Задание 2 . Допишите код, что бы вывести расширенный список
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
print (set(spisok))

# Задание 5. Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно
# присутствует, замените его на 200. Обновите список только при первом вхождении числа
# 20.
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