abc = 'аеиоуыэюя'
text = input('Введите текст:')

letter = [i for i in text if i in abc]
print(f'Список гласных букв:{letter}')
print(f'Длина списка:{len(letter)}')
