zen_file = open('zen.txt', 'r', encoding='utf-8')
data = zen_file.read()
words = dict()
for i_words in data.lower():
    if i_words.isalpha():
        if i_words in words:
            words[i_words] += 1
        else:
            words[i_words] = 1
count = 0
for i_count in words.values():
    count += i_count
print('Количество букв в файле:{count}'.format(count=count))
exeption_words = data.replace('.','').replace("'",'').replace(',','').replace('!','')\
     .replace('-','').replace('*','').replace('\n',' ')
word = exeption_words.split(' ')
len_words = len(word)
print('Количество слов в файле:{len_words}'.format(len_words=len_words))
zen_file.close()
zen_file = open('zen.txt', 'r', encoding='utf-8')
new_data = zen_file.readlines()
iter = 0
for i_iter in new_data:
    iter += 1
print('Количество строк в файле:{iter}'.format(iter=iter))
min_words = min(words, key=words.get)
print('Наиболее редкая буква:{min_words}'.format(min_words=min_words.upper()))
zen_file.close()