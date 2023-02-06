import os

save = input('Введите текст, который хотите сохранить: ')
path = input('Куда хотите сохранить? ')
name = input('Введите название файла(с расширением .txt) ')
end = '.txt'
if not name.endswith(end):
    print('Ошибка, неверное расширение файла(допустимо .txt)!')
else:
    create_path = '/'.join(path.split(' '))
    real_path = os.path.abspath(os.path.join(os.path.sep, create_path))
    if os.path.exists(name):
        confirm = input('Вы действительно хотите перезаписать файл? ')
        if confirm == 'yes':
            file = open(name, 'a', encoding='utf-8')
            file.write(save)
            print('Файл успешно перезаписан!')
            file.close()
            new_path = os.path.abspath(name)
            new_file = open(new_path, 'r', encoding='utf-8')
            print('Содержимое файла:', new_file.read())
            new_file.close()
        else:
            new_path = os.path.abspath(name)
            new_file = open(new_path, 'r', encoding='utf-8')
            print('Содержимое файла:', new_file.read())
            new_file.close()
    else:
        file = open(name, 'w', encoding='utf-8')
        file.write(save)
        print('Файл успешно записан!')
        file.close()
        new_path = os.path.abspath(name)
        new_file = open(new_path, 'r', encoding='utf-8')
        print('Содержимое файла:', new_file.read())
        new_file.close()
