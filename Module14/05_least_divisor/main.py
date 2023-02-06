def delitel(number):
    for i in range(2, number + 1):
        if number % i == 0:
            print(f'Наименьший делитель числа {number} отличный от 1: {i}')
            break


number = int(input('Введите число:'))
delitel(number)

