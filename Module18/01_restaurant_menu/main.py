menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
new_menu = menu.split(';')
new_menu = ', '.join(new_menu)
print('Доступное меню:{menu}'.format(menu=menu))
print('На данный момент в меню есть:{new_menu}'.format(new_menu=new_menu))
