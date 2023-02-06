import random


class Budda:

    CARMA = 500

    def one_day(self):
        day = 0
        carma = 0
        flag = True
        while flag:
            dead = random.randint(1, 10)
            if carma >= self.CARMA:
                flag = False
            else:
                if dead != 10:
                    carma += random.randint(1, 7)
                    day += 1
                    print('День-{day}'.format(day=day))
                    print('Кармы накопленно: {carma}'.format(carma=carma))
                    print()
                else:
                    dead_reason = random.randint(1, 5)
                    if dead_reason == 1:
                        death = KillError()
                        with open('karma.log', 'w', encoding='utf-8') as file:
                            file.write(str(death))
                    elif dead_reason == 2:
                        death = DrunkError()
                        with open('karma.log', 'w', encoding='utf-8') as file:
                            file.write(str(death))
                    elif dead_reason == 3:
                        death = CarCrashError()
                        with open('karma.log', 'w', encoding='utf-8') as file:
                            file.write(str(death))
                    elif dead_reason == 4:
                        death = GluttonyError()
                        with open('karma.log', 'w', encoding='utf-8') as file:
                            file.write(str(death))
                    else:
                        death = DepressionError()
                        with open('karma.log', 'w', encoding='utf-8') as file:
                            file.write(str(death))
                    break
        if flag is False:
            print(f'Поздравляю, вам понадобилось {day} дней чтобы накопить {self.CARMA} кармы!')
        else:
            print("Вы не накопили нужное количество кармы, попытайтесь в следующей жизни, ОМ!")


class KillError(Exception):
    def __init__(self):
        super().__init__('Убийство! К сожалению вас убили!')


class DrunkError(Exception):
    def __init__(self):
        super().__init__('Алкоголизм! Алкоголь не доводит до добра, вы умерли от инфаркта!')


class CarCrashError(Exception):
    def __init__(self):
        super().__init__('Дорожно транспортное происшествие! Никто уже не скажет кто в ней был виноват,факт в том, '
                         'что вы разбились на смерть в автокатастрофе!')


class GluttonyError(Exception):
    def __init__(self):
        super().__init__('Смерть! Вы умерли от проблем вызванных ожирением!')


class DepressionError(Exception):
    def __init__(self):
        super().__init__('Самоубийство! Вы не выдержали бремя бытия и пошли против природы, вас любило так много '
                         'человек, но вы этого уже не узнаете!')


day_carma = Budda()
day_carma.one_day()
