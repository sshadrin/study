class Property():

    def __init__(self, worth):
        self.worth = worth

    def pay(self):
        nalog = self.worth
        return nalog


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.worth = worth / 1000


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.worth = worth / 200


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.worth = worth / 500


while True:
    q = input('Нажмите q для выхода! или любую кнопку для продолжения:').lower()
    if q != 'q':
        money = float(input('Введите ваше количество денег:'))
        worth_apr = float(input('Введите стоимость квартиры:'))
        worth_car = float(input('Введите стоимость машины:'))
        worth_house = float(input('Введите стоимость загородного дома:'))
        apr = Apartment(worth_apr)
        car = Car(worth_car)
        house = CountryHouse(worth_house)
        print()
        print('Ваш налог на квартиру составляет {pay}!'.format(pay=apr.pay()))
        if money > apr.pay():
            print('После уплаты налога у вас останется {pay}'.format(pay=money - apr.pay()))
            print()
        else:
            print('Вам не хватает денег, идите на работу!')
            print()
        print('Ваш налог на машину составляет {pay}!'.format(pay=car.pay()))
        if money > car.pay():
            print('После уплаты налога у вас останется {pay}'.format(pay=money - car.pay()))
            print()
        else:
            print('Вам не хватает денег, идите на работу!')
            print()
        print('Ваш налог на загородный дом составляет {pay}!'.format(pay=house.pay()))
        if money > house.pay():
            print('После уплаты налога у вас останется {pay}'.format(pay=money - house.pay()))
            print()
        else:
            print('Вам не хватает денег, идите на работу!')
            print()
        nalog = apr.pay() + car.pay() + house.pay()
        print('Всего вам необходимо заплатить налогов {all_pay}'.format(all_pay=nalog))
        if money > nalog:
            print('После уплаты всех налогов у вас останется {pay}'.format(pay=money - nalog))
            print()
        else:
            print('У вас дефецит бюджета {pay}!'.format(pay=money - nalog))
    else:
        break

