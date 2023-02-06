import os


def join_path(*args):  # для передачи произвольных аргументов, чтобы найти путь любой интересующей нас директории
    return os.path.join(*args)


def gen_files_path(ls:str, dir=None):  # если каталог не задан перебираем всеь системный диск
    if dir is None:
        dir = os.path.abspath(os.path.sep)
        for i in os.listdir(os.path.join(dir)):  # перебираем только заданную директормю
            if i == ls:
                for j in os.walk(os.path.join(os.path.sep, i)):
                    print(j)
            else:
                for j in os.walk(os.path.join(os.path.sep, i, ls)):
                    print(j)
    else:
        for i in os.listdir(os.path.join(dir)):  # перебираем искомую категорию
            if i == ls:
                for j in os.walk(os.path.join(dir, i)):  # walk выдает все файлы в виде списка
                    print(j)


gen_files_path("CCleaner")
gen_files_path('Python', join_path("C:/","Users","sshad","Desktop"))

