class Animal:
    sounds = {
        "pies": "Hau hau!",
        "kot": "Miau!",
        "królik": "Chrupu chrupu!",
        "kaczka": "Kwa kwa!"
    }

    def introduce(self):
        print(f"Jestem typem {self.type} mam na imię {self.name}, jest nass {self.counter}!")

    def make_sound(self):
        print(self.sounds.get(self.type, "Nie wydaję dźwięków."))


class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        self.name = name
        Dog.counter += 1

    def make_sound(self):
        print("Hau hau!")


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        self.name = name
        Cat.counter += 1



class Rabbit(Animal):
    type = "królik"
    counter = 0

    def __init__(self, name):
        self.name = name
        Rabbit.counter += 1



class Duck(Animal):
    type = "kaczka"
    counter = 0

    def __init__(self, name):
        self.name = name
        Duck.counter += 1



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
    animal.make_sound()
