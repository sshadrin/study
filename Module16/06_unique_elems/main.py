first = 1
second = 1
first_list = []
second_list = []
while first != 4:
    number = int(input(f'Введите {first}-е число для первого списка:'))
    first_list.append(number)
    first += 1

while second != 8:
    number = int(input(f'Введите {second}-е число для второго списка:'))
    second_list.append(number)
    second += 1

print('Первый список:', first_list)
print('Второй список:',second_list)
first_list.extend(second_list)
new_list = list(set(first_list))
print('Новый первый список с уникальными элементами:', new_list)
