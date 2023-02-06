goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i_keys, j_values in goods.items():
   total = 0
   price = 0
   for number in store[j_values]:
       number_quantity = number['quantity']
       number_price = number['price']
       price = number_quantity * number_price
       total += number_quantity
   print('{name} - {quantity} шт, общая стоимость {price} рублей.'.format(name=i_keys,quantity=total, price=price))
