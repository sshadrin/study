violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number = int(input('Введите количество:'))
end = 1
count = 0
while end != number + 1:
    name = input('Название {end}-й песни:'.format(end=end))
    if name in violator_songs:
        count += violator_songs[name]
        end += 1
    else:
        print('Данной песни в списке нет')


print('Общее время звучания песен: {count} минут'.format(count=round(count, 2)))

