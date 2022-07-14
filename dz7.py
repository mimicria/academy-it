#!/usr/bin/python3

# Коллекции

# Задача 1. Каждый ученик в классе изучает либо английский, либо французский, либо
# оба этих языка. У классного руководителя есть списки учеников, изучающих английский и
# французский языки. Помогите ему выяснить, сколько учеников в классе изучают только
# один язык.
# Формат ввода: В первых двух строках указывается количество учеников, изучающих
# английский и французский языки (M и N). Затем идут M+N строк с фамилиями учеников в
# произвольном порядке. Гарантируется, что среди учеников нет однофамильцев. Формат
# вывода: Количество учеников, которые изучают только один язык. Если таких учеников не
# окажется, в строке вывода нужно написать 0.

import collections

while True:
    try:
        M = int(input('Количество англ.: '))
        N = int(input('Количество фр.: '))
        break
    except ValueError:
        print('Введите числа')
        continue
fam = []
for i in range(M+N):
    fam.append(input())
l2d = collections.Counter(fam)
cnt = 0
for v in l2d.values():
    if v==1:
        cnt+=1
print('Один язык изучают ',cnt)

# Задача 2. Начальник отдела кадров хочет узнать, сколько мужчин-однофамильцев
# работает в организации. Имеется список фамилий, и на основании этого списка нужно
# вычислить количество фамилий, которые совпадают с другими.
# Формат ввода: В первой строке указывается количество мужчин — сотрудников
# организации (N). Затем идут N строк с фамилиями этих сотрудников в произвольном
# порядке.
# Формат вывода: Количество однофамильцев в организации.

while True:
    try:
        N = int(input('Количество: '))
        break
    except ValueError:
        print('Введите число')
        continue
fam = []
for i in range(N):
    fam.append(input())
l2d = collections.Counter(fam)
cnt = 0
for v in l2d.values():
    if v>1:
        cnt+=v
print('Однофамильцев: ',cnt)

# Задача 3. Возьмём число. Умножим его на его же первую цифру. Результат умножим на
# первую цифру результата. И так далее. Например, начнём с 3:
# 3 → 3 * 3 = 9
# 9 → 9 * 9 = 81
# 81 → 81 * 8 = 648
# 648 → 648 * 6 = 3888
# 3888 → 3888 * 3 = 11664
# 11664 → 11884 * 1 = 11664
# Очевидно, когда первая цифра очередного числа в такой последовательности
# становится равной 1, числа перестают изменяться. Но это происходит не при всех
# начальных числах.
# Напишите программу, которая будет хотя бы приблизительно определять судьбу
# введённого числа.
# Формат ввода: Вводится натуральное число n, меньшее миллиарда.
# Формат вывода: Начиная с числа n, умножайте имеющееся число на его первую цифру,
# пока у получившегося числа первая цифра не станет равной 1, либо пока оно не превысит
# миллиарда. Выведите результат.
# Пример 1. Ввод: 3. Вывод: 11664.
# Пример 2. Ввод: 5. Вывод:.

n = input('Введите число: ')             # Не понял как тут применить коллекции
while int(n) < 1000000000:
    n = str(int(n) * int(n[0]))
    if n[0] == '1':
        print(n)
        break

# Задача 4. Числа Трибоначчи — это последовательность целых чисел, которая
# определяется так:
# первое, второе и третье числа Трибоначчи равны единице;
# каждое следующее число Трибоначчи равно сумме трёх предыдущих.
# Напишите программу, которая вычисляет числа Трибоначчи.
# Например. Вводим 6, получаем 1 1 1 3 5 9

trib = [1,1,1]                     # Не понял как тут применить коллекции
n = int(input('Введите число: '))
for i in range(3,n):
    trib.append(sum(trib[-3:]))
print(trib)

# Задача 5. Частотный анализ — это подсчёт, какие символы чаще встречаются в тексте.
# Это важнейший инструмент взлома многих классических шифров — от шифра Цезаря до
# шифровальной машины «Энигма». Выполним простой частотный анализ: выясним, какой
# символ чаще всего встречается в данном тексте.
# Программа запрашивает одну строку. Выводит один символ в нижнем регистре —
# наиболее часто встречающийся во введённой строке, кроме пробела, без учёта регистра,
# если таких несколько — выводится первый по алфавиту.

str = input().lower()
lol = list(str)
while lol.count(' ')>0:
    lol.remove(' ')
print(collections.Counter(lol).most_common(1))

# Задача 6. Напишите функцию, которая принимает один словарь, и возвращает другой, в
# котором ключами являются значения из первого словаря, а значениями –
# соответствующие им ключи.
# Создайте словарь, передайте его в функцию. Выведите на экран исходный и
# "перевернутый" словари.

def dict_invert(d):                     # Не понял как тут применить коллекции
    res = {v:k for k,v in d.items()}
    return res

d1 = { "Калина": 7, "Гранта": 9, "Volvo": 15 }
d2 = dict_invert(d1)
print(d1)
print(d2)
