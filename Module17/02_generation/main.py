number = int(input('Введите длину списка:'))

arr = [(1 if i % 2 == 0 else i % 5) for i in range(number)]
print(arr)