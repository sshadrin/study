import os


def join_path(*args):  # для передачи произвольных аргументов, чтобы найти путь любой интересующей нас директории
    return os.path.join(*args)


def gen_files_path(ls: str, dir: str) -> list:
    arr = list()
    for i_dir in os.listdir(os.path.join(dir)):  # перебираем искомую категорию
        if i_dir == ls:  # находим нашу категорию, начинаем безумие
            for j_files in os.walk(os.path.join(dir, i_dir)):  # перебираем все файлы в нашей категории
                for k_string in j_files:  # поскольку возвращается кортеж, перебираем его и ишем нужные папки и файлы
                    if type(k_string) == str:  # если тип строка, соответственно это путь до папки
                        path = k_string  # запоминаем этот путь в переменную
                    for l_py in k_string:  # ищем только необходимые файлы с расширением .py
                        if l_py.endswith(".py"):
                            arr.append(os.path.join(dir, i_dir, path, l_py))  # добавляем в список нужные пути
    return arr  # возвращаем список для работы с файлами


iter = 0  # счетчик для подсчета строк
sumary = list()  # сумму каждого файла запишем как элемент списка
for i_file in gen_files_path('Module26', join_path("C:/", "Users", "sshad", "Desktop", "Python", "dpo_python_basic")):
    with open(i_file, 'r', encoding='utf-8') as file:  # перебираем каждый файл
        for i_string in file.readlines():  # считаем строки
            if i_string != '\n' and not i_string.startswith("#"):
                iter += 1
        sumary.append(iter)  # записываем в список

print("Всего строчек кода во всех файлах .py без учета переноса строки и комментариев: {s}!".format(s=sum(sumary)))
