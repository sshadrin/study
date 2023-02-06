import random


class Parents:

    childrens = list()
    action = {1: 'Успокоить ребёнка.', 2: 'Покормить ребёнка.', 3: 'Все отлично!'}

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_age(self, other, name, age):
        if self.age < other + 16:
            print('Ошибка, неправильный возраст ребенка!')
        else:
            self.childrens.append(name)
            self.childrens.append(age)

    def children_info(self):
        for i in range(len(self.childrens)):
            if i % 2 == 0:
                print(self.childrens[i], end='  ')

    def mother_info(self):
        print('Здравствуйте, меня зовут {name}, мой возраст в годах: {age}.'.format(name=self.name, age=self.age))

    def do_action_food(self):
        print('Необходимо:', self.action[2])

    def do_action_cry(self):
        print('Необходимо:', self.action[1])

    def do_action_rest(self):
        print(self.action[3])


class Children:

    condition = {1: 'голоден и хочет кушать!', 2: 'спокоен как удав!', 3: 'Сильно плачет!'}
    save_condition = list()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def status(self):
        flag = random.randint(1, 3)
        if flag == 1:
            self.save_condition.append(1)
            print('Ребенок {name} {status}'.format(name=self.name, status=self.condition[1]))
        elif flag == 2:
            self.save_condition.append(2)
            print('Ребенок {name} {status}'.format(name=self.name, status=self.condition[2]))
        else:
            self.save_condition.append(3)
            print('Ребенок {name} {status}'.format(name=self.name, status=self.condition[3]))


mother = Parents('Dasha', 34)
mother.mother_info()
daughter = Children('Polina', 5)
mother.check_age(daughter.age, daughter.name, daughter.age)
daughter.status()
if daughter.save_condition == [1]:
    mother.do_action_food()
elif daughter.save_condition == [3]:
    mother.do_action_cry()
else:
    mother.do_action_rest()


daughter_1 = Children('Masha', 15)
mother.check_age(daughter_1.age, daughter_1.name, daughter_1.age)
print('Список моих детей:')
mother.children_info()