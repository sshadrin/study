number = int(input('Введите количество заказов:'))
count = 1
dictyonary = dict()

while count != number + 1:
    zakaz = input('Заказ №-{count}:'.format(count=count))
    zakaz = zakaz.split(' ')
    name = zakaz[0]
    pizza = zakaz[1]
    value = int(zakaz[2])
    if name not in dictyonary:
        dictyonary[name] = {pizza:value}
    else:
        if pizza not in dictyonary[name]:
            dictyonary[name][pizza] = value
        else:
            dictyonary[name][pizza] += value
    count += 1
for i_name, zakaz in dictyonary.items():
    print('{name}:'.format(name=i_name))
    for i_pizza, i_value in zakaz.items():
        print('  {pizza}:{value}'.format(pizza=i_pizza,value=i_value))





