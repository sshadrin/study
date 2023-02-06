import random


class House:

    money = 100
    food = 50
    cat_food = 30
    dirt = 0

    def dirty(self):
        self.dirt += 5


class Husband(House):

    satiety = 30
    happy = 100
    f = 0

    def __init__(self, name):
        self.name = name

    def eat(self):
        eat = random.randint(10, 30)
        print("{name} съел {eat} едениц еды!".format(name=self.name, eat=eat))
        self.satiety += eat
        House.food -= eat
        self.f = eat

    def play(self):
        print("{name} играет в кудахтер!".format(name=self.name))
        self.satiety -= 10
        self.happy += 20

    def work(self):
        print("{name} пошел на работу!".format(name=self.name))
        self.satiety -= 10
        House.money += 150

    def cat_play(self):
        print("{name} гладит кота!".format(name=self.name))
        self.satiety -= 10
        self.happy += 5


class Waifu(House):

    satiety = 30
    happy = 100
    f = 0

    def __init__(self, name):
        self.name = name

    def eat(self):
        eat = random.randint(10, 30)
        print("{name} съел {eat} едениц еды!".format(name=self.name, eat=eat))
        self.satiety += eat
        House.food -= eat
        self.f = eat

    def buy(self):
        print("{name} пошла за покупками!".format(name=self.name))
        print("{name} купила поесть!".format(name=self.name))
        House.money -= 20
        self.satiety -= 10
        House.food += 120
        House.cat_food += 10

    def fur_coat(self):
        print("{name} купила себе новую шубку!".format(name=self.name))
        House.money -= 350
        self.happy += 60
        self.satiety -= 10

    def clean(self):
        print("{name} прибралась в доме!".format(name=self.name))
        self.satiety -= 10
        dirt = random.randint(10, 100)
        House.dirt -= dirt
        if House.dirt < 0:
            House.dirt = 0

    def cat_play(self):
        print("{name} гладит кота!".format(name=self.name))
        self.satiety -= 10
        self.happy += 5


class Cat(House):

    satiety = 30
    f = 0

    def __init__(self, name):
        self.name = name

    def eat(self):
        eat = random.randint(1, 10)
        print("{name} съел {eat} едениц еды!".format(name=self.name, eat=eat))
        self.satiety += eat * 2
        House.cat_food -= eat
        self.f = eat

    def sleep(self):
        print("{name} дрыхнет!".format(name=self.name))
        self.satiety -= 10

    def play(self):
        print("{name} дерет обои!".format(name=self.name))
        self.satiety -= 10
        House.dirt += 5


dom = House()
husband = Husband("Sol")
wife = Waifu("Dasha")
cat = Cat("Musya")
day = 1
year = 367
coat = 0
food = 0
money = 0
flag = True
while day != year:
    print(f"{day}-й день!")
    if husband.satiety <= 0 and wife.satiety <= 0 and cat.satiety <= 0:
        dictionary = {husband.name: husband.satiety, wife.name: wife.satiety, cat.name: cat.satiety}
        for i, j in dictionary.items():
            if j <= 0:
                print("Случилось несчатье {name} умер от голода!".format(name=i))
        flag = False
        break
    elif husband.happy <= 10 and wife.happy <= 10:
        dictionary = {husband.name: husband.happy, wife.name: wife.happy}
        for i, j in dictionary.items():
            if j <= 0:
                print("Случилось несчатье {name} умер от депрессии!".format(name=i))
        flag = False
        break
    else:
        if dom.food < 60:
            husband.work()
            money += 150
            wife.buy()
            cat.sleep()
            husband.eat()
            wife.eat()
            cat.eat()
        else:
            if dom.dirt > 90:
                husband.satiety -= 10
                wife.satiety -= 10
            square = random.randint(1, 10)
            if square == 1:
                husband.cat_play()
                wife.cat_play()
                cat.sleep()
            elif square == 2:
                husband.play()
                fur_coat = random.randint(1, 10)
                if fur_coat == 10 and House.money > 350:
                    wife.fur_coat()
                    coat += 1
                else:
                    wife.buy()
                cat.sleep()
            elif square == 3:
                husband.work()
                money += 150
                wife.clean()
                cat.play()
            else:
                husband.eat()
                wife.eat()
                cat.eat()
        dom.dirty()
        print("Итоги дня!")
        print("Денег в доме: {money} рублей.".format(money=dom.money))
        print("Еды в холодильнике: {food} едениц.".format(food=dom.food))
        print("Кошачей еды в доме: {food} едениц.".format(food=dom.cat_food))
        print("Уровень загрязнения дома: {dirt} едениц".format(dirt=dom.dirt))
        print("Уровень сытости {name}a: {satiety} едениц.".format(name=husband.name, satiety=husband.satiety))
        print("Уровень счастья {name}a: {happy} едениц.".format(name=husband.name, happy=husband.happy))
        print("Уровень сытости {name}a: {satiety} едениц.".format(name=wife.name, satiety=wife.satiety))
        print("Уровень счастья {name}a: {happy} едениц.".format(name=wife.name, happy=wife.happy))
        print("Уровень сытости {name}a: {satiety} едениц.".format(name=cat.name, satiety=cat.satiety))
        food += husband.f + wife.f + cat.f
        day += 1
print()
if flag is True:
    print("Поздравляем вы прожили целый год!")
    print(f"За год вы заработали {money} рублей!")
    print(f"За год вы съели {food} кг еды!")
    print(f"За год вы купили {coat} шуб!")
else:
    print("Соболезнуем!")
