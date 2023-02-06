family = {('Иванов', 'Иван'): 47,
          ('Иванов', 'Петр'): 21,
          ('Иванова', 'Света'): 24,
          ('Петров', 'Иван'): 40,
          ('Петрова', 'Анна'): 36,
          ('Петров', 'Петр'): 16,
          ('Петрова', 'Света'): 20,
          ('Сидров', 'Иван'): 30,
          ('Сидрова', 'Анна'): 30,
          ('Сидров', 'Петр'): 5,
          ('Сидрова', 'Света'): 6}


surname = input('Введите фамилию:').title()
new_surname = surname + 'а'
for i_family, j_values in family.items():
    if i_family[0] == surname or i_family[0] == new_surname:
        print(i_family[0], i_family[1], j_values)
