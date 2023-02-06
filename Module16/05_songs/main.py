violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
new_song = []
for i in violator_songs:
    new_song.extend(i)
print(new_song)
n = int(input('Введите количество треков:'))
a = 0
time = 0
while a != n:
    song = input('Введите название песни:')
    count = 0
    if song not in new_song:
        print('Таких песен в нашем плейлисте нету!')
    else:
        for j in range(len(violator_songs)):
            if violator_songs[j][0] == song:
                count += violator_songs[j][1]
        a += 1
        print(f'Название {a} песни:{song}')
        time += count
print(f'Общее время звучания песен: {time} минуты')



