
class Animal:
    total_counter = 0

    def introduce(self):
        print(f"Jestem typem {self.type}, mam na imię {self.name}. Jest nas {self.counter} w moim gatunku i {Animal.total_counter} ogółem!")
        self.make_sound()

    def define_all(self):
        print(f"Dotychczas utworzona liczba zwierząt: {self.total_counter}.")

class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        self.name = name
        Dog.counter += 1
        Animal.total_counter += 1


    def make_sound(self):
        print("Wydawany odgłos: hau hau!")


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        self.name = name
        Cat.counter += 1
        Animal.total_counter += 1

    def make_sound(self):
        print("Wydawany odgłos: miau!")


class Rabbit(Animal):
    type = "królik"
    counter = 0

    def __init__(self, name):
        self.name = name
        Rabbit.counter += 1
        Animal.total_counter += 1

    def make_sound(self):
        print("Wydawany odgłos: chrupu chrupu!")  # W sumie to nie wiem jak robi królik :|


class Duck(Animal):
    type = "kaczka"
    counter = 0

    def __init__(self, name):
        self.name = name
        Duck.counter += 1
        Animal.total_counter += 1


    def make_sound(self):
        print("Wydawany odgłos: kwa kwa!")




animals = [
    Dog("Pluto"),
    Dog("As"),
    Dog("Azor"),
    Cat("Filemon"),
    Rabbit("Bugs"),
    Duck("Duffy")
]

for animal in animals:
    animal.introduce()

