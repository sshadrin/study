import typing
import functools
import datetime


def logging(func: typing.Callable) -> typing.Callable:
    """Создаем декоратор который будет записывать возникающие ошибки(исключения) в специальный log файл"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        """Создаем функцию заглушку, которая будет выполняться перед основной функцией"""
        print(func.__doc__)  # Выводим документацию
        try:  # для отлова используем try, except
            value = func(*args, **kwargs)
        except Exception as e:  # если выскакивает исключение, записываем его в файл
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                print("Во время работы функции были обнаружены ошибки! Подробности в function_errors.log")
                file.write("Функция {f}. Ошибка:{e} {t}!\n".format(f=func.__name__, e=type(e).__name__,
                                                                   t=datetime.datetime.now()))
        else:
            return value  # если все нормально
    return wrapped_func


@logging  # найдем относительную погрешность суммы двух приближенных чисел
def approximate_sum(a: float, b: float, delta_a: float, delta_b: float) -> float:
    """Название функции: approximate_sum.
Функция предназначена для вычисления относительной погрешности двух приближенных чисел. В функцию
передаются числа и их абсолютные погршности, функция возвращает относительную погрешность суммы этих чисел.
Тип возвращаемого значения :return float"""
    summa = a + b
    delta_sum = delta_a + delta_b
    sigma_sum = (delta_sum / summa) * 100
    return round(sigma_sum, 4)

@logging
def error(x: int, y:int) -> float:
    """Название функции: error.
    Функция предназначена для генерирования ошибки ZeroDivisionError"""
    error = x / y
    return error



approximate = approximate_sum(3.6, 1.98, 0.01, 0.02)
print(approximate)

e = error(10, 0)
print(e)