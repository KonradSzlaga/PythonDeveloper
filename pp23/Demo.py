
"""
class MyClass:
    y = 99

    def my_method(self, x):
        self.other_method()
        print("To jest moja metoda", x, self.y)



# Self może się rpzydać gdy chcemy się odwołać do innegj metody
    # np wywołanie other_method w czasie wywoływania my_method


    def other_method(self):
        print("To jest inna metoda", self.y)



obj = MyClass()
obj.my_method(1)

"""

"""
class MyClass:
    def __init__(self, name):
        print("Inicjalizuję metodę...")
        self.__name = name

    def get_name(self):
        return self.__name

obj = MyClass("jaro")
print(obj.get_name())

"""

class MyClass:
    def __my_private_method(self):
        print("To jest metoda niepubliczna.")

obj = MyClass()
#obj.__my_private_method()     # Nie działa więc sprawdzmy co jest w klasie
print(MyClass.__dict__)
obj._MyClass__my_private_method()





