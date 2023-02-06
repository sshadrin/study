text = input('Введите текст:')
frequency = dict()
new_frequency = dict()
for sym in text:
    if sym in frequency:
        frequency[sym] += 1
    else:
        frequency[sym] = 1
print('Стандартная гистограмма:')
for i_keys in frequency:
    print(i_keys, ':', frequency[i_keys])
print('Инвертированная гистограмма:')
for i_sym, j_num in frequency.items():
    new_frequency.setdefault(j_num, []).append(i_sym)
for i_keys in new_frequency:
    print('{keys} : {values}'.format(keys=i_keys, values=new_frequency[i_keys]))