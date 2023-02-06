import random

number = int(input('Введите длину списка:'))
arr = [random.randint(0, 2) for i in range(number)]
new_arr = [j for j in arr if j != 0]

print('Количество чисел в списке:', number)
print('Список до сжатия:', arr)
print('Список после сжатия:', new_arr)

