file = open('text.txt', 'r',encoding='utf-8')
read = file.read()
file.close()
frequency = dict()
for i_sym in read.lower():
    if i_sym.isalpha():
        if i_sym in frequency:
            frequency[i_sym] += 1
        else:
            frequency[i_sym] = 1
sum_values = 0
for i_values in frequency.values():
    sum_values += i_values
print('Всего буквы встречаются', sum_values, 'раз.')
new_frequency = dict()
for i_key, j_values in frequency.items():
    new_frequency[i_key] = round(j_values / 12, 3)
sort_alfa = sorted(new_frequency.items(), key=lambda x: (x[1] * -1, x[0]))
final_dict = dict(sort_alfa)
new_file = open('analysis.txt', 'w',encoding='utf-8')
final_string = ''.join('{} {} \n'.format(name, score) for name, score in final_dict.items())
new_file.write(str(final_string))
new_file.close()
new_file = open('analysis.txt', 'r',encoding='utf-8')
print(f'Содержимое файла analysis.txt:\n{new_file.read()}')
new_file.close()