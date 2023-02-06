import random


class Fight:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def info(self):
        print('У {name} сейчас:{hp} хит поинтов!'.format(name=self.name, hp=self.hp))

    def punch(self):
        self.hp = self.hp - 20

    def win(self, other, name):
        if self.hp > other:
            print('Победитель сегодня: {name}!'.format(name=self.name))
        else:
            print('Победитель сегодня: {name}!'.format(name=name))

war_1 = Fight('Воин Джек', 100)
war_1.info()
war_2 = Fight('Воин Джорж', 100)
war_2.info()
count = 1
while war_1.hp != 0 and war_2.hp != 0:
    turn = random.randint(1, 2)
    print(f'Раунд № {count}:')
    if turn == 1:
        print('{name} наносит удар!'.format(name=war_1.name))
        war_2.punch()
        war_1.info()
        war_2.info()
    else:
        print('{name} наносит удар!'.format(name=war_2.name))
        war_1.punch()
        war_1.info()
        war_2.info()
    count += 1
war_1.win(war_2.hp, war_2.name)
