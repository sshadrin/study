list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def finder(x: list, y: list, find: int):  # Обернем код в функцию
    for i in x:
        for j in y:
            result = i * j
            print(i, j, result)
            if result == find:
                return (yield "Found!!!")  # Возвращаем генератор и StopItteration на искомом значении


generation = finder(list_1, list_2, to_find)
for i in generation:
    print(i)
