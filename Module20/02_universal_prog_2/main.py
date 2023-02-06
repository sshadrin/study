def crypto(iter_obj):
    a = list()
    for i_index in is_prime(iter_obj):
        for i_number, j_value in enumerate(iter_obj):
            if i_number == i_index:
                a.append(j_value)
    return a


def is_prime(text):
    text = len(text)
    sypher = list()
    for i in range(2, text + 1):
        count = 0
        if i == 2:
            sypher.append(i)
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count == 1:
            sypher.append(i)
    sypher = sorted(list(set(sypher)))
    return sypher


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
