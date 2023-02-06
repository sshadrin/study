def revers(number):
    parts = str(number).split('.')
    parts[0] = ''.join(reversed(list(str(parts[0]))))
    parts[1] = ''.join(reversed(list(str(parts[1]))))
    return float(parts[0] + '.' + parts[1])


number = float(input('Введите первое число:'))
number_1 = float(input('Введите второе число:'))
revers_number = revers((number))
revers_number_1 = revers((number_1))
print(f'Первое число наоборот:{revers_number}')
print(f'Второе число наоборот:{revers_number_1}')
print(f'Сумма перевернутых чисел:{revers_number + revers_number_1}')







