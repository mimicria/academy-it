#!/usr/bin/python3

# Файлы

# Задание 1. Создайте файл nums.txt, содержащий несколько чисел, записанных через
# пробел. Напишите программу, которая подсчитывает и выводит на экран общую сумму
# чисел, хранящихся в этом файле.

with open('files/nums.txt', 'r') as f:
    nums = f.read().split()
total = 0
for i in nums:
    total += int(i)
print(total)


# Задание 2. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее
# максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r') as f:
        words = f.read().split()
    return max(words, key=len)


print(longest_words('files/article.txt'))


# Задание 3. Напишите функцию reverse(in_file, out_file), которая читает строки из
# файла in_file и создает файл out_file, куда сохраняет прочитанные строки в обратном
# порядке.

def reverse(in_file, out_file):
    with open(in_file, 'r') as f:
        lines = f.readlines()
    lines.reverse()
    with open(out_file, 'w') as f:
        f.writelines(lines)


reverse('files/article.txt', 'files/article_rev.txt')

# Задание 4. В многострочном текстовом файле prices.txt каждая строка с помощью
# символа табуляции разделена на три колонки:
# 1. название товара,
# 2. количество товара и
# 3. цена за 1 шт.
# Выведите общую стоимость заказа с точностью до копеек.

import re

with open('files/prices.txt', 'r') as f:
    tlist = re.split('\t|\n', f.read())
total = 0.0
for i in range(1, len(tlist), 3):
    total += float(tlist[i]) * float(tlist[i + 1])
print(total)
