text = input('Введите текст:')
new_text = text.split()
count = 0
for i in new_text:
    if len(i) > count:
        count = len(i)
print('Самое длинное слово:', max(new_text, key=len))
print('Длина этого слова: {count}'.format(count=count))



