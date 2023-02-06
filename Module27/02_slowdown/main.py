import typing
import functools
import time


def sleeping(func: typing.Callable) -> typing.Callable:
    """Создаем декоратор который будет замедлять работу любой функции"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        """Создаем функцию заглушку, которая будет выполняться перед основной функцией"""
        time.sleep(10)  # используем модуль time для задержки в 10 сек
        value = func(*args, **kwargs)  # выполняем нашу функцию
        return value
    return wrapped_func


@sleeping
def approximate_sum(a: float, b: float, delta_a: float, delta_b: float) -> float:
    """Функция которая вычисляет относительную погрешность суммы двух приблеженных чисел с округлением до 4 знаков"""
    summa = a + b
    delta_sum = delta_a + delta_b
    sigma_sum = (delta_sum / summa) * 100
    return round(sigma_sum, 4)


approximate = approximate_sum(3.6, 1.98, 0.01, 0.02)
print(approximate)