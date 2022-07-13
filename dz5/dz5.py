#!/usr/bin/python3
# Создайте пакет 'figures', состоящий из двух подпакетов: 'triangle', 'square'. В каждом
# подпакете будем иметь файл code.py, где создадим ряд функций:
# – для пакета 'triangle': функции triangle_perimeter() – вычисляет периметр
# треугольника, triangle_area() – вычисляет площадь фигуры.
# На вход функциям передается длина трех сторон.
# – для пакета 'square': функции square_perimeter() – вычисляет периметр квадрата,
# square_area() – вычисляет площадь фигуры.
# Ваша итоговая задача – позволить человеку, загрузившему ваш пакет, иметь
# возможность напрямую импортировать все функции из подпакетов.
# После импорта пакета, запросите у пользователя параметры треугольника и
# квадрата, после этого выдаются вычисляемые значения фигур
# Постарайтесь сделать код таким, чтобы это не заставило вас переписывать все
# внутренние импорты с учетом нового именования.


from figures import triangle_type, triangle_perimeter, triangle_area, square_area, square_perimeter

print('Введите стороны треугольника')
try:
    a = float(input("Введите A: "))
    b = float(input("Введите B: "))
    c = float(input("Введите C: "))
    print(f'Периметр: {triangle_perimeter(a,b,c)}, площадь: {triangle_area(a,b,c)}, тип: {triangle_type(a,b,c)}')
except ValueError:
    print(f'Периметр: {triangle_perimeter()}, площадь: {triangle_area()}, тип: {triangle_type()}')

try:
    a = float(input("Введите сторону квадрата A: "))
    print(f'Периметр: {square_perimeter(a)}, площадь: {square_area(a)}')
except ValueError:
    print(f'Периметр: {square_perimeter()}, площадь: {square_area()}')
