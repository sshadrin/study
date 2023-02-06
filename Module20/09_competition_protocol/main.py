result = dict()
string = int(input('Сколько записей вносится в протокол?'))
elem = 1
for time in range(string):
    score, name = input(f'{elem}-ая запись:').split()
    score = int(score)
    if name in result:
        if score > result[name][0]:
            result[name][0] = score
            result[name][1] = time
    else:
        result[name] = [score, time]
    elem += 1
scores = list(result.items())


def score_key(a):
    return a[1][0]*100000000 - a[1][1]


scores.sort(key=score_key, reverse = True)
for winner_index in 0, 1, 2:
    print(winner_index + 1, 'место.', scores[winner_index][0], end =' ')
    print('(', scores[winner_index][1][0], ')', sep='')






