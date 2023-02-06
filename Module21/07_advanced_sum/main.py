def my_sum(args):
    sum = 0
    for i in args:
        if isinstance(i, (list, tuple)):
            sum += my_sum(i)
        elif isinstance(i, int):
            sum += i
        else:
            raise TypeError("unsupported object of type: {}".format(type(i)))
    return sum

print(my_sum([[1, 2, [3]], [1], 3]))