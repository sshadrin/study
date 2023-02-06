class Iterator:  # Реализация класса итератор

    def __init__(self, number):
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.number:
            self.count += 1
            return self.count ** 2
        else:
            raise StopIteration


print("Реализация класса!")
iteration = Iterator(5)
for i in iteration:
    print(i)
print()

print("Реализация функции генератора!")


def square(number):  # Реализация функции генератора
    for n_number in range(number + 1):
        yield n_number ** 2


for i_number in square(7):
    print(i_number)
print()

print("Реализация генераторного выражения!")
num_gen = [num ** 2 for num in range(10)]  # Реализация генераторного выражения
for j in num_gen:
    print(j)