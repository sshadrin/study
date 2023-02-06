containers = int(input('Введите количество контейнеров:'))
arr = []
if containers > 10:
    print('На склад не помещается больше 10 контейнеров!')
else:
    count = 0
    while count < containers:
        mass = int(input('Введите вес контейнера:'))
        if mass > 200:
            print('Не допустимая масса контейнера')
        else:
            arr.append(mass)
            count += 1

print('Список масс котейнеров:', arr)
arr.sort(reverse=True)
new_mass = int(input('Введите вес нового контейнера:'))
elem = 1
for i in arr:
    if i >= new_mass:
        elem += 1
print('Номер, который получит новый контейнер:', elem)


