shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
new_shop = []
for i in shop:
    new_shop.extend(i)
print(new_shop)
detail = input('Введите название детали:')
if detail not in new_shop:
    print('Таких деталей в нашем магазине нету!')
else:
    pay = 0
    for j in range(len(shop)):
         if shop[j][0] == detail:
            pay += shop[j][1]
    print('Количество деталей на складе:', new_shop.count(detail))
    print('Общая стоимость:', pay)


