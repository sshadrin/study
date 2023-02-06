first = int(input('Введите количество коньков:'))
first_count = 1
first_list = []
while first_count != first + 1:
    number = int(input(f'Введите размер {first_count}-й пары:'))
    first_list.append(number)
    first_count += 1
print()
second = int(input('Введите количество людей:'))
second_count = 1
second_list = []
while second_count != second + 1:
    number = int(input(f'Введите размер ноги {second_count}-го человека:'))
    second_list.append(number)
    second_count += 1
print('Первый список:', first_list)
print('Второй список:', second_list)
min_size = min(second_list)
mens = 0
for i in first_list:
    if i >= min_size:
        mens += 1
print(f'Наибольшее кол-во людей, которые могут взять ролики:{mens}')
