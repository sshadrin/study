text = input('Введите строку:')
word = 'h'
arr = []
count = 0

for i in text:
    if i == word:
        arr.append(count)
    count += 1

new_arr = []
new_arr.append(arr[0])
new_arr.append(arr[-1])
slice_first = int(new_arr[0])
slice_second = int(new_arr[1]) - 1

print('Развёрнутая последовательность между первым и последним h:', text[slice_second:slice_first:-1])


