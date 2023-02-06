def validator(code):
    try:
        flag = True
        if len(code) != 3:
            flag = False
            with open('registrations_bad.log', 'a', encoding='utf-8') as file:
                file.write('{alfa} {symbol} {age}          '
                           'НЕ присутствуют все три поля!\n'.format(alfa=alfa, symbol=symbol, age=age))
                raise IndexError('НЕ присутствуют все три поля!')
        alfa = code[0]
        symbol = code[1]
        age = int(code[2])
        for i_sym in alfa:
            if not i_sym.isalpha():
                flag = False
                with open('registrations_bad.log', 'a', encoding='utf-8') as file:
                    file.write('{alfa} {symbol} {age}          '
                            'Поле имени содержит НЕ только буквы!\n'.format(alfa=alfa, symbol=symbol, age=age))
                    raise NameError('Поле имени содержит НЕ только буквы!')
        if  '@' not in symbol or '.' not in symbol:
            flag = False
            with open('registrations_bad.log', 'a', encoding='utf-8') as file:
                file.write('{alfa} {symbol} {age}          '
                            'Поле «Имейл» НЕ содержит @ или .(точку)!\n'.format(alfa=alfa, symbol=symbol, age=age))
                raise SyntaxError('Поле «Имейл» НЕ содержит @ или .(точку)!')
        if age < 10 or age > 99:
            flag = False
            with open('registrations_bad.log', 'a', encoding='utf-8') as file:
                file.write('{alfa} {symbol} {age}          '
                            'Поле «Возраст» НЕ является числом от 10 до 99!\n'.format(alfa=alfa, symbol=symbol, age=age))
                raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99!')
        if flag == True:
            with open('registrations_good.log', 'a', encoding='utf-8') as file:
                file.write('{alfa} {symbol} {age}\n'.format(alfa=alfa, symbol=symbol, age=age))
    except:
        pass


with open('registrations.txt', 'r', encoding='utf-8') as file:
    string = file.readlines()
    for i in string:
        split = i.split()
        validator(split)

with open('registrations_bad.log', 'r', encoding='utf-8') as file:
    print('Содержимое файла registrations_bad.log:')
    print(file.read())
with open('registrations_good.log', 'r', encoding='utf-8') as file:
    print('Содержимое файла registrations_good.log:')
    print(file.read())
