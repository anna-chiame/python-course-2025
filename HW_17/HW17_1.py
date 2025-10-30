# Task 1

class Animal :

    def __init__(self, name):
        self.name = name

    def talk(self):
        return f"Animal {self.name} says something"

class Dog(Animal) :

     def __init__(self, name) :
         self.name = name

     def talk(self):
         return  f"Dog {self.name} says Woof-Woof "

class Cat(Animal) :

    def __init__(self, name) :
        self.name = name

    def talk(self):
        return f"Cat {self.name} says Meow"

pets = [Dog("Rex"), Cat ("Mira")]
for pet in pets :
    print(pet.talk())