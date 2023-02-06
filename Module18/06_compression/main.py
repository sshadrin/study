text = input('Введите текст:')
array = [i for i in text]
array.append('*')
new_array = []
count = 0
elem = 0
while count != len(array) - 1:
    if array[elem] == array[elem + 1] and array[elem] != array[elem - 1]:
        new_array.append(array[elem])
    elif array[elem] != array[elem + 1] and array[elem] != array[elem - 1]:
        new_array.append(array[elem])
    elem += 1
    count += 1
lenth = 0
width = 0
number = []
iter = 1
while lenth != len(array) - 1:
    if array[width] == array[width + 1]:
        iter += 1
    elif array[width] != array[width + 1] and array[width] != array[width - 1]:
        number.append(1)
    else:
        number.append(iter)
        iter = 1
    lenth += 1
    width += 1
finaly = []
for k, l in zip(new_array, number):
    finaly.append(k + str(l))
finaly = ''.join(finaly)
print('Закодированная строка:{finaly}'.format(finaly=finaly))
