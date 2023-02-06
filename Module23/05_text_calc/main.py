def calc(data):
    result = 0
    number_1 = int(data[0])
    symbol = data[1]
    number_2 = int(data[2])
    sym = '+ - * /'
    try:
        if symbol not in sym:
            print('В строке:{number_1} {symbol} {number_2} обнаружена ошибка!'.format(
                number_1=number_1, symbol=symbol, number_2=number_2))
            correct = input('Хотите исправить?')
            if correct == 'Да':
                new = input('Введите исправленную строку:' )
                new = new.split()
                number_1 = int(new[0])
                symbol = new[1]
                number_2 = int(new[2])
                if symbol == '+':
                    result = number_1 + number_2
                elif symbol == '-':
                    result = number_1 - number_2
                elif symbol == '*':
                    result = number_1 * number_2
                elif symbol == '/':
                    result = number_1 / number_2
                return result
        else:
            if symbol == '+':
                result = number_1 + number_2
            elif symbol == '-':
                result = number_1 - number_2
            elif symbol == '*':
                result = number_1 * number_2
            elif symbol == '/':
                result = number_1 / number_2
    except FileNotFoundError:
        print('Файл не найден!')
    finally:
        return result


print('Содержимое консоли:')
with open('calc.txt', 'r', encoding='utf8') as file:
    read = file.readlines()
    result = 0
    for i in read:
        split = i.split()
        result += calc(split)
print('Сумма результатов:{result}'.format(result=result))