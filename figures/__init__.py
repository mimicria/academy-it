# Ваша итоговая задача – позволить человеку, загрузившему ваш пакет, иметь
# возможность напрямую импортировать все функции из подпакетов.
# Например, он может написать так: 'from figure import square_perimeter '.

from .square.code import square_perimeter,square_area
from .triangle.code import triangle_area, triangle_type, triangle_perimeter
