# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
# Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']

print(my_list[2])
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

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
# мама, папа, Юля, Нина, Мурка
# мама, папа, Максим
# мама, папа, Максим, Пиф
# мама, папа, Максим, Пиф, Лиза

family_1 = tuple(input('Введите текст через запятую: ').split(','))
family_2 = tuple(input('Введите текст через запятую: ').split(','))
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print('family_1')
else:
    print('family_2')

print('_____________________________')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

film = {
    'title': 'Девчата',
    'director': 'Юрий Чулюкин',
    'year': 1961,
    'budget': 100000,
    'main_actor_1': 'Надежда Румянцева',
    'actor_2': 'Николай Рыбников',
    'slogan': 'Я вообще решила замуж не выходить. Одной спокойнее, хочу халву ем, хочу пряники.'
}

print(film.keys())
print(film.values())
print(film.items())

print('_____________________________')

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

print(sum(my_dictionary.values()))

print('_____________________________')

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

my_set = {1, 2, 3, 4, 5, 3, 2, 1}

print(set([1, 2, 3, 4, 5, 3, 2, 1]))

print('_____________________________')

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
set3 = {'a', 'z', 1, 5, 9, 12, 100, 'b', 'd'}

print(set1.intersection(set2))
print(set2.difference(set1))
print(set2.intersection(set1))
print(set1.difference(set2))
print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set1.issubset(set3))










