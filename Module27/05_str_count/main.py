import typing
import functools


def counter(func: typing.Callable) -> typing.Callable:
    """Создаем декоратор который будет увеличивать счетчик вызванной основной функции на +1, за каждый вызов"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):  # заглушка
        wrapped_func.count += 1   # при каждом вызове задекорируемой функции увеличиваем счетчик
        value = func(*args, **kwargs)  # выполняем нашу функцию
        print("Функция {n} была вызвана: {c}-раз.".format(n=func.__name__, c=wrapped_func.count))
        return value
    wrapped_func.count = 0  # счетчик
    return wrapped_func


@counter
def square(x: int):
    """Функция для возведения числа в квадрат"""
    return x ** 2


print(square(5))
print(square(6))
print(square(7))