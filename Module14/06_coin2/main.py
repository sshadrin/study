import math


def coordinate(x, y, r):
    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    if hypotenuse <= r:
        print('Монетка где-то рядом.')
    else:
        print('Монетки в области нет.')


x = float(input('Введите координату монетки по оси X:'))
y = float(input('Введите координату монетки по оси Y:'))
area = int(input('Введите радиус:'))

coordinate(x, y, area)