class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def introduce(self):
        return(f"Mam na imie {self.__name} a mój wiek to {self.__age} lat.")

obj1 = Person("Konrad", 35)
obj2 = Person("Ola", 38)


print(obj1.introduce())
print(obj2.introduce())