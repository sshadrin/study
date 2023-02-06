numbers = int(input('Введите максимальное число:'))
all_nums = set(range(1, numbers + 1))
while True:
    guess = input('Нужное число есть среди вот этих чисел:')
    if guess == 'Помогите!':
        break
    guess = guess.split()
    guess = {int(i) for i in guess}
    answer = input('Ответ Артёма:')
    if answer == 'Да':
        all_nums &= guess
    else:
        all_nums -= guess
print('Артём мог загадать следующие числа:', *all_nums)
