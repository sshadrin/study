guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    welcome = input('Человек пришел или ушел?').lower()
    if welcome == 'пришел' and len(guests) < 6:
        name = input('Введите имя друга, который пришел:')
        guests.append(name)
        print('Сейчас в гостях', len(guests), 'человек:', guests)
    elif welcome == 'ушел':
        exit = input('Кто ушел:')
        if exit not in guests:
            print('Такого человека нет в доме!')
        else:
            guests.remove(exit)
            print('Сейчас в гостях:', len(guests), 'человек:', guests)
    elif welcome == 'пора спать':
        print('Спокойной ночи!')
        break
    else:
        print('В доме не может быть больше 6 человек!')
