friend = int(input('Количествово друзей:'))
receipt = int(input('Долговых расписок:'))
friends_list = []
for _ in range(friend):
    friends_list.append(0)
for number in range(receipt):
    print()
    print(f'{number + 1}-я расписка')
    who = int(input('Кому:'))
    from_who = int(input('От кого:'))
    how_much = int(input('Сколько:'))
    friends_list[from_who - 1] += how_much
    friends_list[who - 1] -= how_much
print()
print('Баланс друзей:')
for i in range(len(friends_list)):
    print(f'{i + 1} : {friends_list[i]}')
