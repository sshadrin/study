import random

number = int(input('Введите количество клеток:'))
cells = []
for i in range(0, number):
    i = random.randint(0, 9)
    cells.append(i)
print('Эффективность клеток:', cells)

non_cells = []
for j, elem in enumerate((cells), start=1):
    print(f'Эффективность {j} клетки:{elem}')
    if elem > j:
        non_cells.append(j - 1)
print()
print('Неподходящие значения:', non_cells, end='')
