import random

arr = []
number = int(input('Введите количество элементов массива:'))
for i in range(number):
    arr.append(random.randrange(-100, 100))

print('Неотсортированный массив:', arr)
arr.sort()
print('Отсортированный массив по возрастанию элементов:', arr)
