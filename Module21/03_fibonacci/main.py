def numbers(num):
    if num in (1, 2):
        return 1
    return numbers(num - 1) + numbers(num - 2)


num = int(input('Введите позицию числа в ряде Фибоначчи:'))
print(f'Число:{numbers(num)}')