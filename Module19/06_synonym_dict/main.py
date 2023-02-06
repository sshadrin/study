number = int(input('Введите количество пар слов синонимов:'))
count = 1
dictionary = dict()
while count != number + 1:
    text = input('{count}-ая пара:'.format(count=count)).lower()
    sym = ' - '
    text = text.split(sym)
    value = text[1]
    dictionary[text[0]] = value
    count += 1
print(dictionary)
while True:
    words = input('Введите слово:').lower()
    if words in dictionary:
        print('Синоним для данного слова в словаре: {value}'.format(value=dictionary.get(words)))
        break
    else:
        print('Такого слова в словаре нет.')




