import my_calc
import my_methods

# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

def square(a=5):
    b = a * 4
    c = a * 2
    d = a * a + a * a
    return b, c, d

print(square())
print(my_calc.line)


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def figure(name = "John", last_name = 'Smith', age = 35, position = 'web developer'):
    return f' name = \033[96m\033[4m{name}\033[0m\n last_name = \033[96m\033[4m{last_name}\033[0m\n ' \
           f'age =  \033[96m\033[4m{age}\033[0m\n position = \033[96m\033[4m{position}\033[0m'

print(figure())
print(my_calc.line)

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
# содержащий только положительные числа

my_list = [20, -3, 15, 2, -1, -21]

print(list(filter(lambda x: x >= 0, my_list)))
print(my_calc.line)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

import functools

print(functools.reduce(lambda x, y: x * y, my_list))
print(my_calc.line)

# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле

res = my_calc.sum_it(10, 12)
print(res)

res1 = my_calc.prod_it(45, 6)
print(res1)

print(my_calc.line)

def test():
    assert my_methods.div(10, 0) == 'Can`t divide by zero'

print(my_calc.end)












