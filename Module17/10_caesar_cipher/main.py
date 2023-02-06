def caesar(text, step):
    list = [(alfa[(alfa.index(sym) + step) % 33] if sym != ' ' else ' ') for sym in text]
    new_list = ''
    for i in list:
        new_list += i
    return new_list


alfa = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите строку:')
step = int(input('Введите шаг:'))

cipher = caesar(text, step)
print('Зашифрованное сообщение:', cipher)
