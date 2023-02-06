class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        if age in range(18, 65):
            self.__age = age
        else:
            raise Exception("Возраст должен быть от 18 дп 65!")

    def __str__(self):
        return "{name} {surname}(возраст {age})".format(name=self.__name, surname=self.__surname, age=self.__age)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employ(Person):

    def __init__(self, name, surname, age, pay):
        super().__init__(name, surname, age)
        self.pay = pay

    def get_pay(self):
        pay = self.pay
        return pay


class Manager(Employ):

    __pay = 13000

    def __init__(self, name, surname, age, pay):
        super().__init__(name, surname, age, pay)

    def get_pay(self):
        pay = self.__pay
        return pay


class Agent(Employ):
    __pay = 5000

    def __init__(self, name, surname, age, pay, sell):
        super().__init__(name, surname, age, pay)
        self.__sell = sell * 0.05

    def get_pay(self):
        pay = self.__pay + self.__sell
        return pay


class Worker(Employ):

    __pay = 100
    __hour = 160

    def __init__(self, name, surname, age, pay):
        super().__init__(name, surname, age, pay)
        self.__pay = self.__pay

    def set_hour(self, hour):
        self.__hour = hour

    def get_pay(self):
        pay = self.__pay * self.__hour
        return pay


manager_jack = Manager("Jack", "Nikolson", 25, 'null')
print("Manager:{name}. Зарплата: {pay}!".format(name=manager_jack.__str__(), pay=manager_jack.get_pay()))
agent_jonny = Agent("Jonny", "Depp", 22, 'null', 70000)
print("Agent:{name}. Зарплата: {pay}!".format(name=agent_jonny.__str__(), pay=agent_jonny.get_pay()))
worker_jim = Worker("Jim", "Beem", 35, 'null')
print("Worker:{name}. Зарплата: {pay}!".format(name=worker_jim.__str__(), pay=worker_jim.get_pay()))
manager_andrew = Manager("Andrew", "Andreev", 40, 'null')
print("Manager:{name}. Зарплата: {pay}!".format(name=manager_andrew.__str__(), pay=manager_andrew.get_pay()))
agent_phil = Agent("Phil", "Smith", 18, 'null', 50000)
print("Agent:{name}. Зарплата: {pay}!".format(name=agent_phil.__str__(), pay=agent_phil.get_pay()))
worker_bily = Worker("Billy", "Star", 33, 'null')
print("Worker:{name}. Зарплата: {pay}!".format(name=worker_bily.__str__(), pay=worker_bily.get_pay()))
manager_kris = Manager("Kris", "Kelmy", 55, 'null')
print("Manager:{name}. Зарплата: {pay}!".format(name=manager_kris.__str__(), pay=manager_kris.get_pay()))
agent_super = Agent("Nikolas", "Best", 35, 'null', 1000000)
print("Agent:{name}. Зарплата: {pay}!".format(name=agent_super.__str__(), pay=agent_super.get_pay()))
worker_serg = Worker("Serg", "Shad", 34, 'null')
worker_serg.set_hour(220)
print("Worker:{name}. Зарплата: {pay}!".format(name=worker_serg.__str__(), pay=worker_serg.get_pay()))
