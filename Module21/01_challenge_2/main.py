num = int(input('Введите число:'))
i = 0


def numbers(i):
    i += 1
    if i != num + 1:
        print(i)
        numbers(i)


numbers(i)