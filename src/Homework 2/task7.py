"""
Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь. Если нет, вывести сообщение о неверных данных.

"""
s = 0
a, b, c = 12, 13, 15
divisor = 2
degree = 0.5
print(a, b, c)
if not a + b > c and c + b > a and a + c > b:
    print('Введены неверные данные')
else:
    p = (a + b + c) / divisor
    buffer = p * (p - a) + (p - b) * (p - c)
    s = buffer ** degree
    print('Площадь треугольнка S:', s)
