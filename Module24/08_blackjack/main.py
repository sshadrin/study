import random


class Deck:

    suit = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    deck_1 = list()
    deck = dict()

    for i_suit in suit:
        for j_value in value:
            deck_1.append(str(j_value) + '-' + i_suit)

    value_1 = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    value_2 = ['Jack', 'Queen', 'King']
    value_3 = ['Ace']

    for i_suit in deck_1:
        for j_value in value_1:
            if i_suit.startswith(j_value):
                deck[i_suit] = int(j_value)

    for i_suit in deck_1:
        for j_value in value_2:
            if i_suit.startswith(j_value):
                deck[i_suit] = int(10)

    for i_suit in deck_1:
        for j_value in value_3:
            if i_suit.startswith(j_value):
                deck[i_suit] = int(11)


class Player:

    sum_value = 0

    def __init__(self, name):
        self.name = name

    def begin(self):
        n = 0
        while n != 2:
            if self.sum_value >= 11:
                Deck.deck['Ace-Hearts'] = 1
                Deck.deck['Ace-Diamonds'] = 1
                Deck.deck['Ace-Spades'] = 1
                card = random.choices(list(Deck.deck.items()))
                print('Выполучили карту {name}'.format(name=card[0]))
                self.sum_value += card[0][1]
                print('У вас на руках {value} очков.'.format(value=self.sum_value))
                del card
            else:
                card = random.choices(list(Deck.deck.items()))
                print('Выполучили карту {name}'.format(name=card[0]))
                self.sum_value += card[0][1]
                print('У вас на руках {value} очков.'.format(value=self.sum_value))
                del card
            n += 1

    def play(self):
        while self.sum_value < 21:
            take = input('Хотите взять карту?(Да/Нет): ')
            if take == 'Да':
                if self.sum_value >= 11:
                    Deck.deck['Ace-Hearts'] = 1
                    Deck.deck['Ace-Diamonds'] = 1
                    Deck.deck['Ace-Spades'] = 1
                    card = random.choices(list(Deck.deck.items()))
                    print('Выполучили карту {name}'.format(name=card[0]))
                    self.sum_value += card[0][1]
                    print('У вас на руках {value} очков.'.format(value=self.sum_value))
                    del card
                else:
                    card = random.choices(list(Deck.deck.items()))
                    print('Выполучили карту {name}'.format(name=card[0]))
                    self.sum_value += card[0][1]
                    print('У вас на руках {value} очков.'.format(value=self.sum_value))
                    del card
            else:
                print('У вас на руках {value} очков.'.format(value=self.sum_value))
                break


class Computer:

    sum_value = 0

    def __init__(self, name):
        self.name = name

    def begin(self):
        n = 0
        while n != 2:
            if self.sum_value >= 11:
                Deck.deck['Ace-Hearts'] = 1
                Deck.deck['Ace-Diamonds'] = 1
                Deck.deck['Ace-Spades'] = 1
                card = random.choices(list(Deck.deck.items()))
                self.sum_value += card[0][1]
                del card
            else:
                card = random.choices(list(Deck.deck.items()))
                self.sum_value += card[0][1]
                del card
            n += 1


player_human = Player('Serg')
player_computer = Computer('OpenAI2023')
player_human.begin()
player_computer.begin()
player_human.play()
if player_human.sum_value > 21:
    print('Перебор, вы проиграли!')
elif player_human.sum_value == player_computer.sum_value:
    print('Сегодня обошлись ничьей, победила дружба!')
elif player_computer.sum_value > player_human.sum_value:
    print('{name} набрал {value} очков. Вы {name_1} набрали {value_1} очков'.format(
        name=player_computer.name, value=player_computer.sum_value,
        name_1=player_human.name, value_1=player_human.sum_value))
    print('{name}, победил вас, тренеруйтесь еще!'.format(name=player_computer.name))
else:
    print('{name} набрал {value} очков. Вы {name_1} набрали {value_1} очков'.format(
        name=player_computer.name, value=player_computer.sum_value,
        name_1=player_human.name, value_1=player_human.sum_value))
    print('Вы победили бездушную машину, так держать!')