import random

lucky_number = 777
n = 0
try:
    with open('out_file.txt', 'w', encoding='utf-8') as file:
        while n < lucky_number:
            number = int(input('Введите число:'))
            n += number
            unluck = random.randint(1, 13)
            file.write('{n}\n'.format(n=str(number)))
            if unluck == 13:
                raise BaseException()
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
    with open('out_file.txt', 'r', encoding='utf-8') as file:
        print('Содержимое файла out_file.txt:')
        print(file.read())
except BaseException:
    print('Something wrong!')
    print('Вас постигла неудача!')
    with open('out_file.txt', 'r', encoding='utf-8') as file:
        print('Содержимое файла out_file.txt:')
        print(file.read())