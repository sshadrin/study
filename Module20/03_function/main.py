def slicer(tupple, sym):
    sym = sym
    arr = list(tupple)
    new_arr = list()
    count = 0
    for i_sym in arr:
        if i_sym == sym:
            count += 1
    if sym not in arr:
        return tuple()
    if count == 1:
        index = arr.index(sym)
        arr = arr[index:]
        return tuple(arr)
    if count >= 2:
        index = arr.index(sym)
        arr = arr[index:]
        elem = 0
        for i_index in arr:
            new_arr.append(i_index)
            if i_index == sym:
                elem += 1
                if elem == 2:
                    break
        return tuple(new_arr)


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
