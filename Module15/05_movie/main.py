films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
spisok = []
number = int(input('Сколько фильмов хотите добавить?'))
count = 0
if number > 10:
    print('В данный момент к добавлению доступно только 10 фильмов!')
else:
    while count < number:
        title = input('Введите название фильма:')
        if title in films:
            print('Добавлено!')
            spisok.append(title)
        else:
            print(f'Ошибка: фильма {title} у нас нет :(')
        count += 1

print('Ваш список любимых фильмов:', spisok)
