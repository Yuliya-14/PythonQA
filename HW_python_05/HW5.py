import my_methods

class Dogs:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def plays(self):
        return "Играть с собакой!"

    def vaccine(self):
        return "Собака идет на привику :("

    def animal_dogs(self):
        return "Animals is beautiful"

    def get_age(self):
        return f"My dog is {self._age}"

    def set_age(self, newage):
        self._age = newage

class Breed(Dogs):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age)
        self.breed = breed

    def sleeps(self):
        return "Собака любит спать!!"

    def animal_dogs(self):
        return "sleeps"


class Color(Dogs):
    def __init__(self, nickname, age, breed, color):
        super().__init__(nickname, age)
        self.breed = breed
        self.color = color

    def hairstyle(self):
        return "Собака идет на стрижку :)"

    def animal_dogs(self):
        return "Style"


dog1 = Dogs('Piff', 3)
print(dog1.nickname)
print(dog1.age)
print(dog1.plays())
print(dog1.vaccine())
print(dog1.animal_dogs())

print(my_methods.line)

dog2 = Breed('Alex', 12, 'Овчарка')
print(dog2.nickname)
print(dog2.age)
print(dog2.breed)
print(dog2.sleeps())
print(dog2.plays())
print(dog2.vaccine())
print(dog2.animal_dogs())

print(my_methods.line)

dog3 = Color('Зверюга', 5, 'Волкодав', 'Grey')
print(dog3.nickname)
print(dog3.age)
print(dog3.breed)
print(dog3.color)
print(dog3.plays())
print(dog3.hairstyle())
print(dog3.vaccine())
print(dog3.animal_dogs())

print(my_methods.line)



