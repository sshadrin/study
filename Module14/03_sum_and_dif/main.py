def summ(number):
    count = 0
    for i in str(number):
        count += int(i)
    print(f'Сумма цифр введенного числа:{count}')
    return count


def quantity(number):
    elem = 0
    for i in str(number):
        elem += 1
    print(f'Количество цифр в числе:{elem}')
    return elem


number = int(input('Введите число:'))

print(f'Разность суммы и количества цифр:{summ(number) - quantity(number)}')

