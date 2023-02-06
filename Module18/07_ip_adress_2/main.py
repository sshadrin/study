ip = input('Введите ip:')
split_ip = ip.split('.')
if len(split_ip) < 4:
    print('Адрес - это четыре числа, разделённые точками')
else:
    count = 0
    elem = 0
    for i in split_ip:
        if i.isdigit():
            count += 1
            if int(i) > 255:
                elem += 1
                print(i, 'превышает 255')
        else:
            print(i, '- не целое число')
    if elem == 0 and count == 4:
        print('ip-адрес корректен')
