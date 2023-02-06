class Cell:

    pole = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]

    def info_pole(self):
        print(self.pole[0],  self.pole[1],  self.pole[2])
        print(self.pole[3],  self.pole[4],  self.pole[5])
        print(self.pole[6],  self.pole[7],  self.pole[8])

    def check_win(self):
        win = ''
        win_coord = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for cell in win_coord:
            if self.pole[cell[0]] == 'X' and self.pole[cell[1]] == 'X' and self.pole[cell[2]] == 'X':
                win = "Победитель игрок выбравший - 'X'"
            if self.pole[cell[0]] == 'O' and self.pole[cell[1]] == 'O' and self.pole[cell[2]] == 'O':
                win = "Победитель игрок выбравший - 'O'"
        return win


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def step(self):
        step = int(input('Куда ходим?'))
        if step in Cell.pole:
            move = Cell.pole.index(step)
            Cell.pole[move] = self.symbol
        else:
            print('Клетка занята или отсутствует!')


game = Cell()
serg = Player('Serg', 'X')
computer = Player('DeepMind', 'O')

flag = False

while flag == False:
    game.info_pole()
    print('Ход игрока {name}'.format(name=serg.name))
    serg.step()
    game.info_pole()
    print('Ход игрока {name}'.format(name=computer.name))
    computer.step()
    win = game.check_win()
    if win != '':
        flag = True
        print(win)
    else:
        flag = False
    if all(isinstance(x, str) for x in Cell.pole):
        print('Ничья, победила дружба!')
        break
