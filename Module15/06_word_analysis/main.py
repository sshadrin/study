word = input('Введите слово:').lower()
elem = 0
word = list(word)

for i in word:
    count = 0
    for j in word:
        if i == j:
            count += 1
    if count == 1:
        elem += 1
print('Количество уникальных букв:', elem)
