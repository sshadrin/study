import os

text = 'Hello\nHello\nHello\nHello'
file = open('text.txt', 'w', encoding='utf-8')
file.write(text)
file.close()
alfabet = 'abcdefghijklmnopqrstuvwxyz'
path = os.path.abspath(os.path.join('text.txt'))
read_file = open(path, 'r', encoding='utf-8')
read = read_file.read()
list = list()
count = 1
iter = 0
for i_first in read.lower():
    if i_first == '\n':
        count += 1
    if iter == 6:
        list.append(':')
        iter = 0
    iter += 1
    for j_first in alfabet:
        if i_first == j_first:
            index = alfabet.index(j_first) + count
            list.append(alfabet[index])
split = ''.join(list)
split = split.replace(':','\n').title()
print(f'Содержимое файла text.txt:\n{read}')
file.close()
file = open('cipher_text.txt', 'w', encoding='utf-8')
file.write(split)
file.close()
print()
file = open('cipher_text.txt', 'r', encoding='utf-8')
print(f'Содержимое файла answer.txt:\n{split}')
file.close()


