import random

spisok = []
number = int(input('Введите количество элементов массива:'))
for i in range(number):
    spisok.append(random.randrange(-10, 10))
step = int(input('Введите шаг:'))
print('Изначальный список:', spisok)
print('Сдвиг:', step)
new_spisok = spisok[-step:] + spisok[:-step]
print('Сдвинутый список:', new_spisok)


