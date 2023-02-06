import math


class MyMath:
    """Наш математический модуль. Во всех методах используем декоратор:classmethod
    так как обращаемся не к методам экземпляра класса, а непосредственно к методам класса."""

    @classmethod
    def circle_len(cls, radius: float) -> float:
        """Вычисляем длину окружности"""
        circle_len = 2*(math.pi * radius)
        return circle_len

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """Вычисляем площадь окружности"""
        circle_sq = math.pi * radius ** 2
        return circle_sq

    @classmethod
    def volume_sq(cls, length: float) -> float:
        """Вычисляем объем куба"""
        volume_sq = length ** 3
        return volume_sq

    @classmethod
    def sphere_sq(cls, radius: float) -> float:
        """Вычисляем площадь поверхности сферы"""
        sphere_sq = 4 * math.pi * radius ** 2
        return sphere_sq

    @classmethod
    def delta_sum(cls, x: float, y: float, delta_x: float, delta_y: float) -> float:
        """Вычисляем абсолютную погрешность произведения двух приближенных чисел"""
        sigma_x = delta_x / x
        sigma_y = delta_y / y
        ssum = x * y
        sigma_sum = sigma_x + sigma_y
        delta_sum = ssum * sigma_sum
        return delta_sum