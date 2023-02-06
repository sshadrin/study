zen_file = open('zen.txt', 'r', encoding='utf-8')
data = zen_file.read()
zen_split = data.split('\n')
zen_reverse = zen_split[::-1]
for i in zen_reverse:
    print(i)
zen_file.close()