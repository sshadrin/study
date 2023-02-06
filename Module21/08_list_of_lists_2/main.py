nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def new_list(nice_list):
    for i in nice_list:
        if isinstance(i, list):
            for j in new_list(i):
                yield j
        else:
            yield i

print(list(new_list(nice_list)))