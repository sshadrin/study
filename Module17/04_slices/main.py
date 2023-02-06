alphabet = 'abcdefg'

print('Копия строки:', alphabet[:])
print('Элементы строки в обратном порядке:', alphabet[::-1])
print('Каждый второй элемент строки (включая самый первый):', alphabet[::2])
print('Каждый второй элемент строки после первого:', alphabet[1::2])
print('Все элементы до второго:', alphabet[:1])
print('Все элементы начиная с конца до предпоследнего:', alphabet[:5:-1])
print('Все элементы в диапазоне индексов от 3 до 4 (не включая 4):', alphabet[3:4])
print('Последние три элемента строки:', alphabet[4:])
print('Все элементы в диапазоне индексов от 3 до 4:', alphabet[3:5])
print('Все элементы в диапазоне индексов от 3 до 4, но в обратном порядке:', alphabet[4:2:-1])