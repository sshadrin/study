try:
    with open('people.txt', 'r', encoding='utf-8') as file:
        split = (file.read()).split('\n')
        count = 0
        for i in split:
            length = len(i)
            count += 1
            if length < 3:
                print(f'Ошибка: менее трёх символов в строке {count}.')
                with open('errors.log', 'a', encoding='utf-8') as log:
                    log.write(f'Ошибка: менее трёх символов в строке {count}.\n')
except FileNotFoundError:
    print('Такого файла не существует!')
finally:
    with open('people.txt', 'r', encoding='utf-8') as file:
        iter = 0
        for i_sym in file.read():
            if i_sym != '\n':
                iter += 1
        print(f'Общее количество символов: {iter}.')