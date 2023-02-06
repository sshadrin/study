import math


class Car:

    def __init__(self, x, y, corner):
        self.x = x
        self.y = y
        self.corner = corner

    def move(self, distance):
        print("Автомобиль прошел {distance} км и повернул на {corner} градусов.".format(
            distance=distance, corner=self.corner))
        self.x = self.x + distance * math.cos(self.corner)
        self.y = self.y + distance * math.sin(self.corner)

    def __str__(self):
        return "Текущие координаты ({x},{y}).".format(
            x=self.x, y=self.y)


class Bus(Car):

    money = 0
    number_passager = 0

    def __init__(self, x, y, corner):
        super().__init__(x, y, corner)

    def enter(self, number_passager):
        print("Вошли в автобус: {pas} человек.".format(pas=number_passager))
        self.number_passager += number_passager
        pay = 50 * number_passager
        self.money += pay

    def exit(self, number_passager):
        if number_passager > self.number_passager:
            raise Exception("Количество вышедших людей больше чем есть в автобусе!")
        else:
            print("Вышло из автобуса: {pas} человек.".format(pas=number_passager))
            self.number_passager = self.number_passager - number_passager
            return self.number_passager


    def move(self, distance):
        print("Автобус прошел {distance} км и повернул на {corner} градусов.".format(
            distance=distance, corner=self.corner))
        if distance > 100:
            print("Поскольку мы проехали больше 100 км доплатите по 25 рублей!")
            self.money += self.number_passager * 25
        self.x = self.x + distance * math.cos(self.corner)
        self.y = self.y + distance * math.sin(self.corner)


a = Bus(5, 5, 30)
print(a.__str__())
a.enter(5)
print("Сейчас на счету:{r} рублей.".format(r=a.money))
print("Сейчас в автобусе:{n} пасажиров.".format(n=a.number_passager))
a.move(110)
print("Остановка!")
print(a.__str__())
print("Сейчас на счету:{r} рублей.".format(r=a.money))
print("Сейчас в автобусе:{n} пасажиров.".format(n=a.number_passager))
a.enter(3)
print("Сейчас на счету:{r} рублей.".format(r=a.money))
print("Сейчас в автобусе:{n} пасажиров.".format(n=a.number_passager))
a.move(20)
print("Остановка!")
print(a.__str__())
a.exit(7)
print("Сейчас на счету:{r} рублей.".format(r=a.money))
print("Сейчас в автобусе:{n} пасажиров.".format(n=a.number_passager))
a.move(101)
print("Остановка! Станция конечная.")
print(a.__str__())
a.exit(1)
print("Всего заработано за сегодня: {r} рублей.".format(r=a.money))
