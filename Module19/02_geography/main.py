number = int(input('Введите количество стран:'))
end = 1
country = dict()
while end != number + 1:
    map = input('{end}-ая страна:'.format(end=end))
    map_info = map.split()
    slice = map_info[0]
    map_info.pop(0)
    for i_country in map_info:
        country[i_country] = slice
    end += 1
count = 1
while count != 4:
    name = input('{count}-ый город:'.format(count=count))
    if name in country:
        print('Город {name} расположен в стране {value}.'.format(name=name, value=country[name]))
    else:
        print('По городу {name} данных нет.'.format(name=name))
    count += 1