# для пакета 'triangle': функции triangle_perimeter() – вычисляет периметр
# треугольника, triangle_area() – вычисляет площадь фигуры.
from math import sqrt

default_a = 7
default_b = 2
default_c = 8


def triangle_perimeter(a=default_a, b=default_b, c=default_c):
    return a + b + c


def triangle_area(a=default_a, b=default_b, c=default_c):
    pp = triangle_perimeter(a, b, c) / 2
    s = sqrt(pp * (pp - a) * (pp - b) * (pp - c))
    return s

def triangle_type(a=default_a, b=default_b, c=default_c):
    if a==b==c:
        return 'равносторонний'
    elif a==b or b==c or a==c:
        return 'равнобедренный'
    else:
        return 'обычный'