while True:
    password = input('Придумайте пароль:')
    count = 0
    count_1 = 0
    count_2 = 0
    for i in password:
        if i == i.upper():
            count += 1
        for k in range(10):
            if i == str(k):
                count_1 += 1
    count = count - count_1
    for j in password:
        for elem in range(10):
            if j == str(elem):
                count_2 += 1
    if len(password) < 8 or count == 0 or count_2 < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
