number = int(input('Ввдите количество человек:'))
num = int(input('Какое число в считалке?'))
print('Значит, выбывает каждый', num, 'человек.')
players_list = list(range(1, number + 1))
count = 0

for i in range(number - 1):
    print()
    print('Текущий круг людей', players_list)
    start_count = count % len(players_list)
    count = (start_count + num - 1) % len(players_list)
    print('Начало счёта с номера', players_list[start_count])
    print('Выбывает человек под номером', players_list[count])
    players_list.remove(players_list[count])
print()
print('Остался человек под номером', players_list)

