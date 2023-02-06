numbers_file = open('numbers.txt', 'r', encoding='utf-8')
data = numbers_file.read()
arr = []
for i in data:
    if i != ' ' and i != '\n':
        arr.append(int(i))
sum_arr = sum(arr)
numbers_file.close()
answer = open('numbers.txt', 'w', encoding='utf-8')
answer.write(str(sum_arr))
answer.close()
answer = open('answer.txt', 'r', encoding='utf-8')
print('Содержимое файла answer.txt:')
print(answer.read())
answer.close()
