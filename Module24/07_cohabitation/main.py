import random


class Human:

    satiety = 50

    def __init__(self, name):
        self.name = name

    def eat(self):
        self.satiety += 5

    def work(self):
        self.satiety -= 5

    def play(self):
        self.satiety -= 5


class House:

    def __init__(self, food, money):
        self.food = food
        self.money = money

    def store_money(self, money):
        self.money += money

    def store_food(self, food):
        self.food += food

    def spand_money(self, money):
        self.money -= money

    def spand_food(self, food):
        self.food -= food



year = 367
day = 1
dice = random.randint(1, 6)
serg = Human('Sergey')
artem = Human('Artem')
print('{name} и {name_1} снимают жилье на двоих, они договорились, что у них общий холодильник и счет для покупки еды.'
      .format(name=serg.name, name_1=artem.name))
house = House(50, 0)
while day != year:
    if serg.satiety == 0:
        print('Все полохо, {serg} погиб от голода на {day} день, соболезнуем!'.format(serg=serg.name, day=day))
        break
    elif artem.satiety == 0:
        print('Все полохо, {artem} погиб от голода на {day} день, соболезнуем!'.format(artem=artem.name, day=day))
        break
    elif day == 366:
        print('Поздравляем, вы прожили еще один отличный год, он хоть и был трудным, однако надолго вам запомнится!')
    else:
        print(f'День №:{day}.')
        if serg.satiety < 20 and artem.satiety < 20:
            serg.eat()
            house.spand_food(5)
            artem.eat()
            house.spand_food(5)
            print('{serg} вкусно поел!'.format(serg=serg.name))
            print('{artem} вкусно поел!'.format(artem=artem.name))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=serg.name, satiety=serg.satiety))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=artem.name, satiety=artem.satiety))
            print('Холодильник в доме опустел, в нем осталось еды: {food}кг.'.format(food=house.food))
        elif house.food < 10:
            print('{serg} сходил в магазин!'.format(serg=serg.name))
            house.store_food(5)
            house.spand_money(5)
            print('{artem} сходил в магазин!'.format(artem=artem.name))
            house.store_food(5)
            house.spand_money(5)
            print('Холодильник пополнен, в нем осталось еды: {food}кг.'.format(food=house.food))
            print('Были потраченны деньги, на счету осталось: {money} условных едениц.'.format(money=house.money))
        elif house.money < 50:
            serg.work()
            house.store_money(5)
            artem.work()
            house.store_money(5)
            print('Пора на любимую работу {serg}, вперед!'.format(serg=serg.name))
            print('Пора на любимую работу {artem}, вперед!'.format(artem=artem.name))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=serg.name, satiety=serg.satiety))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=artem.name, satiety=artem.satiety))
            print('Полученно ежедневное жалование, на счету осталось: {money} условных едениц.'.format(
                money=house.money))
        elif dice == 1:
            serg.work()
            house.store_money(5)
            artem.work()
            house.store_money(5)
            print('Пора на любимую работу {serg}, вперед!'.format(serg=serg.name))
            print('Пора на любимую работу {artem}, вперед!'.format(artem=artem.name))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=serg.name, satiety=serg.satiety))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=artem.name, satiety=artem.satiety))
            print('Полученно ежедневное жалование, на счету осталось: {money} условных едениц.'.format(
                money=house.money))
        elif dice == 2:
            serg.eat()
            house.spand_food(5)
            artem.eat()
            house.spand_food(5)
            print('{serg} вкусно поел!'.format(serg=serg.name))
            print('{artem} вкусно поел!'.format(artem=artem.name))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=serg.name, satiety=serg.satiety))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=artem.name, satiety=artem.satiety))
            print('Холодильник в доме опустел, в нем осталось еды: {food}кг.'.format(food=house.food))
        else:
            serg.play()
            artem.play()
            print('{serg} сегодня решил поиграть!'.format(serg=serg.name))
            print('{artem} сегодня решил поиграть!'.format(artem=artem.name))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=serg.name, satiety=serg.satiety))
            print('Уровень сытности теперь {name} составляет {satiety}.'.format(name=artem.name, satiety=artem.satiety))
    day += 1