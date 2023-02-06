import math


class Circle:

    def __init__(self, number, x, y, r):
        self.number = number
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        square = round(math.pi, 2) * (self.r ** 2)
        print('площадь окружности №:{number} = {square}'.format(number=self.number, square=square))
        return square

    def perimetr(self):
        perimetr = (round(math.pi, 2)) * 2 * self.r
        print('периметр окружности №:{number} = {perimetr}'.format(number=self.number, perimetr=perimetr))
        return perimetr

    def up(self, k):
        self.r = self.r * k
        print('окружность №:{number} увеличена в {k} раз.'.format(number=self.number, k=k))

    def info(self):
        print('Окружность №:{number} имеет следующие параметры: координата x:{x}, координата y:{y}, радиус '
              'окружности:{r}'.format(number=self.number, x=self.x, y=self.y, r=self.r))

    def is_intersect(self, other):
        var = (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2
        if var == True:
            print('Окружности пересекаются!')
        else:
            print('Окружности не пересекаются!')



circle_1 = Circle(1, 0, 0, 1)
circle_1.info()
circle_1.square()
circle_1.perimetr()
circle_2 = Circle(2, 5, 5, 3)
circle_2.info()
circle_2.square()
circle_2.perimetr()
circle_1.is_intersect(circle_2)