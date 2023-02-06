def sort(tupple):
    arr = list(tupple)
    for element in tupple:
        if not isinstance(element, int):
            return tupple
        else:
            arr = sorted(arr)
            arr_tuple = tuple(arr)
            return arr_tuple


print(sort((6, 3, -1, 8, 4, 10, -5)))
