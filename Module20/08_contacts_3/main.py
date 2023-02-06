phone_book = dict()
while True:
    print('Введите номер действия:')
    print('1. Добавить контакт')
    print('2. Найти человека')
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        name = input('Введите имя и фамилию нового контакта (через пробел):').title()
        phone = int(input('Введите номер телефона:'))
        name = name.split()
        name = tuple(name)
        phone_dict = {name: phone}
        phone_book.update(phone_dict)
        print(phone_book)
    elif choice == 2:
        surname = input('Введите фамилию:').title()
        new_surname = surname + 'а'
        for i_family, j_values in phone_book.items():
            if i_family[1] == surname or i_family[1] == new_surname:
                print(i_family[0], i_family[1], j_values)
    else:
        print('Ошибка ввода!')