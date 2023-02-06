number = int(input('Введите количество чисел:'))
arr = []

for i in range(number):
    arr.append(int(input('Число:')))

count = 0
while arr != arr[::-1]:
    arr.insert(number, arr[count])
    count += 1

print('Нужно приписать чисел:', count)
print('Сами числа:', arr[:count][::-1])
