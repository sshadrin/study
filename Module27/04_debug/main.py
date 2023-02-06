import inspect
import typing
import functools


def debug(func: typing.Callable) -> typing.Callable:
    """Создаем декоратор который будет: вызывать название основной функции с ее аргументами в виде строки;
    название функции и то, что она возвращает в виде строки; возвращение результата функции"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):  # заглушка
        arguments = inspect.getframeinfo(inspect.currentframe().f_back).code_context[0].strip()
        # функция и ее аргументы
        print("Вызывается {f}".format(f=arguments))
        # Название функции и то, что она возвращает
        print("'{f}' вернула значение {n}".format(f=func.__name__,n=repr(func(*args, **kwargs))))
        value = func(*args, **kwargs)
        print(value)  # результат работы функции
        print()
        return value
    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)