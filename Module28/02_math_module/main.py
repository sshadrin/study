from math_module import MyMath
"""Подключаем созданный нами математический модуль math_module и используем класс MyMath"""

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.volume_sq(length=10)
res_4 = MyMath.sphere_sq(radius=7)
res_5 = MyMath.delta_sum(x=3.6, y=0.68, delta_x=0.01, delta_y=0.02)
print("Длина окружности равна: {l}.".format(l=res_1))
print("Площадь окружности равна: {l}.".format(l=res_2))
print("Объем куба равен: {l}.".format(l=res_3))
print("Площадь поверхности сферы: {l}.".format(l=res_4))
print("Абсолютная погрешность произведения двух приближенных чисел: {l}.".format(l=res_5))
print()
print(MyMath.__doc__)