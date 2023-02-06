import random

first_class = [random.randrange(160, 176, 2) for i in range(12)]
second_class = [random.randrange(162, 180, 3) for j in range(15)]
first_class.extend(second_class)
first_class.sort()
print('Отсортированный список учеников:', first_class)