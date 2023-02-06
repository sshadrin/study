user_name = input('Введите ваше имя: ')
while True:
    print('Увидеть чат - введите 1. Добавить сообщение в чат - введите 2.')
    answer = int(input('Что вы хотите(введите 1 или 2)? '))
    if answer == 1:
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Пока, еще ничего нет!\n')
    elif answer == 2:
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write('{user_name}: {new_message}\n'.format(user_name=user_name, new_message=new_message))
    else:
        print('Ошибка ввода!')