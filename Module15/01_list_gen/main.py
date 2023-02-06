number = int(input('Введите число:'))
array = []

for i in range(1, number + 1):
    if i % 2 != 0:
        array.append(i)

print(f'Список всех нечетных чисел от одного до {number}: {array}')
