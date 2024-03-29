import functools


@functools.cache
def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result


cache = functools.cache(calculating_math_func)

print(calculating_math_func(10))