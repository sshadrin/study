import typing
import functools


def how_are_you(func) -> typing.Callable:
    """Создаем функцию декоратор, которая будет надоедать коллегам"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> typing.Any:
        """Создаем обертку функцию обертку"""
        input("Как дела?: ")  # Эти объекты будут надоедать и вызываться перед исполняемой функцией
        print("А у меня не очень! Ладно, держи свою функцию!")
        value = func(*args, **kwargs)  # вызываем основную функцию
        return value
    return wrapped_func


@how_are_you
def test() -> typing.Any:
    # Вызываем декоратор перед функцией, которую хотят выполнить коллеги
    print('<Тут что-то происходит...>')


test()


