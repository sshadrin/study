import math
from abc import ABC


class Figure(ABC):
    """Создаем абстрактный класс Фигура"""
    def __init__(self, length_base, length_edge):
        self._length_base = length_base
        self._length_edge = length_edge

    def set_length_base(self, length):
        self._length_base = length
        return self._length_base

    def get_length_base(self):
        return self._length_base

    def set_length_edge(self, length):
        self._length_edge = length
        return self._length_edge

    def get_length_edge(self):
        return self._length_edge


class Square(Figure):
    """Создаем класс квадрат от Фигуры для определения периметра и площади, передаем в конструктор длину стороны"""
    def __init__(self, length):
        super().__init__(length_base=None, length_edge=None)
        self._length = length

    def perimetr(self):
        """Находим периметр"""
        perimetr = self._length * 4
        return perimetr

    def square(self) -> float:
        """Находим площадь"""
        square = self._length * self._length
        return square


class SurfaceAreaMixin:
    """Создаем класс примесь который будет считать площадь 3д фигур"""
    def __init__(self):
        self.surface = None

    def surface_area(self) -> float:
        surface_area = 0
        for surface in self.surface:
            surface_area += surface

        return surface_area


class Coub(Square, SurfaceAreaMixin):
    """Создаем класс куб для определения площади куба, передаем в конструктор длину стороны квадрата"""
    def __init__(self, length: float):
        super().__init__(length=length)
        self.surface = [Square.square(self), Square.square(self), Square.square(self), Square.square(self),
                        Square.square(self), Square.square(self)]


class Triangle(Figure):
    """Создаем класс равнобежренный треугольник от Фигуры для определения его периметра, площади, и площади основания.
    Передаем в конструктор длину основания и длину ребер"""
    def __init__(self, length_base, length_edge):
        super().__init__(length_base=None, length_edge=None)
        self._length_base = length_base
        self._length_edge = length_edge

    def height(self):
        """Находим высоту равнобедренного треугольника"""
        height = math.sqrt((self._length_edge ** 2) - ((self._length_base / 2) ** 2))
        return round(height, 2)

    def perimetr(self):
        """Находим периметр"""
        perimetr = self._length_base + self._length_edge * 2
        return perimetr

    def square(self):
        """Находим площадь"""
        square = (self.height() * self._length_base) / 2
        return square

    def square_base(self):
        """Находим площадь основания"""
        square_base = (self.get_length_base() ** 2 * math.sqrt(3)) / 4
        return square_base


class Pyramid(Triangle, SurfaceAreaMixin):
    """Создаем класс пирамида для определения площади пирамиды, передаем в конструктор длину основания и ребра"""
    def __init__(self, length_base: float, length_edge: float):
        super().__init__(length_base=length_base, length_edge=length_edge)
        self.surface = [Triangle.square(self), Triangle.square(self), Triangle.square(self), Triangle.square(self),
                        Triangle.square_base(self)]


# Выводим результаты
square = Square(5)
print("Периметр квадрата с длиной стороны {l} равен: {p}.".format(l=square._length, p=square.perimetr()))
print("Площадь квадрата с длиной стороны {l} равна: {p}.".format(l=square._length, p=square.square()))
coub = Coub(6)
print("Площадь куба с площадью одного квадрата равной {l} равна: {p}.".format(l=coub.square(), p=coub.surface_area()))
print()
triangle = Triangle(10, 15)
print("Высота треугольника равна: {h}".format(h=triangle.height()))
print("Периметр тругольника с основанием {l} и ребрами по {r} равен: {p}.".format(
    l=triangle._length_base, r=triangle._length_edge, p=triangle.perimetr()))
print("Пощадь тругольника с основанием {l} и высотой по {h} равна: {p}.".format(
    l=triangle._length_base, h=triangle.height(), p=triangle.square()))
pyramid = Pyramid(10, 15)
print("Площадь Пирамиды с площадью одного треугольника равной {l} и площадью основания равной {b} равна: {p}.".format(
    l=pyramid.square(), b=round(pyramid.square_base(), 2), p=round(pyramid.surface_area(), 2)))