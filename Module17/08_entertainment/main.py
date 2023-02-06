stick = int(input('Количество палок:'))
throw = int(input('Количество бросков:'))
row = ['I'] * stick
for i in range(throw):
    query = 'Бросок ' + str(i + 1) + '. Сбиты палки с номера:'
    while True:
        start = int(input(query)) - 1
        if (start >= 0) and (start <= stick):
            break
    while True:
        end = int(input('по номер:')) - 1
        if (end >= start) and (end <= stick):
            break
    for j in range(start, end + 1):
        row[j] = '.'

result = ''
for elem in row:
    result += elem

print('Результат:', result)