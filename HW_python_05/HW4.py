# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

def square(a=5):
    b = a * 4
    c = a * a
    d = a * a + a * a
    return b, c, d

print(square())
print('_____________________________')


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def figure(name = "John", last_name = 'Smith', age = 35, position = 'web developer'):
    return f' name = {name} \n last_name = {last_name} \n age =  {age} \n position = {position}'

print(figure())
print('_____________________________')

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
# содержащий только положительные числа

my_list = [20, -3, 15, 2, -1, -21]

print(list(filter(lambda x: x > 0, my_list)))
print('_____________________________')

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

import functools

print(functools.reduce(lambda x, y: x * y, my_list))
print('_____________________________')

# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле









