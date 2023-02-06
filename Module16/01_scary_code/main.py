a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print('Количество цифр 5 в списке:', a.count(5))

for i in a:
    if i == 5:
        a.remove(i)

a.extend(c)
print('Количество цифр 3 в списке:', a.count(3))
print('Новый список:', a)