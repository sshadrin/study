word = input('Введите слово:').lower()
new_word = word[::-1]
if word == new_word:
    print('Слово является палиндромом!')
else:
    print('Слово не является палиндромом!')
