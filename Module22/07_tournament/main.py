k = 80
first = {'Ivanov Serg': 80, 'Segeev Petr': 92, 'Petrov Vasiliy': 98, 'Vasiliev Maksim': 78}
firs_string = ''.join('{} {} \n'.format(name, score) for name, score in first.items())
firs_string = f'\n{str(k)}\n' + f'{firs_string}\n'
file = open('first_tour.txt', 'w', encoding='utf-8')
file.write(firs_string)
file.close()
file = open('first_tour.txt', 'r', encoding='utf-8')
data = file.read()
sort_first = sorted(first.items(), key=lambda x:x[1], reverse=True)
sort_first = sort_first[0:2]
second = dict(sort_first)
name = ['V.Petrov', 'P.Segeev']
final = dict(zip(name,list(second.values())))
print('Содержимое файла first_tour.txt:', data)
file.close()
new_file = open('second_tour.txt', 'w', encoding='utf-8')
q = 1
length = 2
for i, j in final.items():
    new = ('{q}) {i} {j}\n'.format(q=q, i=i, j=j))
    q += 1
    new_file.write(new)
new_file.close()
new_file = open('second_tour.txt', 'r', encoding='utf-8')
print(f'Содержимое файла second_tour.txt:\n{length}\n{new_file.read()}')
new_file.close()