import random

first_spisok = [round(random.uniform(5, 10), 2) for i in range(20)]
second_spisok = [round(random.uniform(5, 10), 2) for elem in range(20)]
print(f'Оценки первой команды:{first_spisok}')
print(f'Оценки второй команды:{second_spisok}')
win = [(first_spisok[j] if first_spisok[j] > second_spisok[j] else second_spisok[j]) for j in range(20)]
print(f'Победители тура:{win}')