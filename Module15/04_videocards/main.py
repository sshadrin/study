spisok = [3070, 2060, 3090, 3070, 3090]
count = 0
new_spisok = []

for i in range(len(spisok)):
    if spisok[i] > count:
        count = spisok[i]

for i in range(len(spisok)):
    if spisok[i] != count:
        new_spisok.append(spisok[i])

print('Старый список видеокарт:', spisok)
print('Новый список видеокарт:', new_spisok)
