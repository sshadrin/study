spisok = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
array = []

for i in range(0, len(spisok), 2):
    array.append(spisok[i])


print(f'Первый день:{array}')
