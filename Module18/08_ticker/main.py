first_str = input('Первая строка:')
second_str = input('Вторая строка:')

if first_str == second_str:
    print('Строки одинаковые.')
else:
    if len(first_str) != len(second_str):
        print('Строки имеют разную длину.')
    else:
        step = 1
        flag = False
        for i in range(len(first_str) - 1):
            second_str = second_str[-1] + second_str[:-1]
            if first_str == second_str:
                print('Первая строка получается из второй со сдвигом {step}.'.format(step=step))
                flag = True
                break
            else:
                step += 1
        if not flag:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

