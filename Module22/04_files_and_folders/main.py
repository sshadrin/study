import os

path = os.path.join('../../Module22')
rel_path = os.path.abspath(path)
print('Путь до каталога: {rel_path}'.format(rel_path=rel_path))
dir = os.listdir(rel_path)
count = 0
for i_dir in dir:
    if os.path.isfile(i_dir):
       count -= 1
    count += 1
size = 0
count_file = 0

for i_dir in dir:
    path_dir = os.path.abspath(os.path.join('..', i_dir))
    if os.path.isdir(path_dir):
        for i_files in os.listdir(path_dir):
            file_path = os.path.join(path_dir, i_files)
            size += os.path.getsize(file_path)
            count_file += 1

for i_file in dir:
    path_dir = os.path.abspath(os.path.join('..', i_file))
    if os.path.isfile(path_dir):
        count_file += 1
        size += os.path.getsize(i_file)

real_size = size // 1024
print('Размер каталога (в Кб): {real_size} Кб'.format(real_size=real_size))
print('Всего подкатологов в папке: {count}'.format(count=count))
print('Всего файлов в каталоге: {count_file}'.format(count_file=count_file))
