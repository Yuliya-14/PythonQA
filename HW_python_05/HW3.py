# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
# Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']

print(my_list[2])

print('_____________________________')

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

#Using lambda and filter
print(sum(filter(lambda x: isinstance(x, int), list_1)))

#Using list comprehension
print([x for x in list_1 if isinstance(x, str) and 'a' in x])

print('_____________________________')

# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж

animal = ['cat', 'dog', 'horse', 'cow']
animal_1 = tuple(animal)

print(animal_1)

print('_____________________________')

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#   Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')









