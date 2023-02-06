filename = input('Введите название файла:')
sym = '@,№,$,%,^,&,*,()'
new_sym = sym.split(',')
if not filename.endswith('.txt') or filename.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    for i in sym:
        if filename.startswith(i):
            print('Ошибка: название начинается на один из специальных символов, которые запрещены.')
            break
        else:
            print('Файл назван верно!')
            break
