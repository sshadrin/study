def my_zip(*args):
    length = min(len(element) for element in args)
    tpl_list = [tuple(struct[i] for struct in map(list, args)) for i in range(length)]
    return tpl_list


syms_str = 'abc'
nums_tpl = [10, 20, 30, 40]

print(my_zip(syms_str, nums_tpl))