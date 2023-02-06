import random

# arr = [random.randint(1, 100) for i_index in range(10)]  Первый вариант решения
# arr_first = list()
# arr_second = list()
# for i in range(len(arr)):
#     if i % 2 == 0:
#         arr_first.append(arr[i])
#     else:
#         arr_second.append(arr[i])
# print('Оригинальный список:', arr)
# arr_first = tuple(arr_first)
# arr_second = tuple(arr_second)
# print('Новый список кортежей:', list(zip(arr_first, arr_second)))

arr = [random.randint(1, 100) for i_index in range(10)]  # Второй вариант решения (лучший наверное)
arr_tuple_first = tuple(arr[::2])
arr_tuple_second = tuple(arr[1::2])
print('Оригинальный список:', arr)
print('Новый список кортежей:', list(zip(arr_tuple_first, arr_tuple_second)))
