class MyClass:

    counter = 0

    def __init__(self, x = 1):
        self.x = x # mzmienna instancji
        MyClass.counter += 1  # Odwołanie do zmiennej klasy

#     #Można zrobić metodę, która przypisuje do obiektu
#     def sety(self, y = 2):
#         self.y = y
# obj = MyClass()
# print(obj.x)
# obj1 = MyClass(15)
# print(obj1.x)
# obj1.sety(58)
# print(obj1.y)
# print(obj1.__dict__)
# print(MyClass.__dict__)

class1 = MyClass()
print(class1.counter)
class2 = MyClass()
print(class2.counter)
class3 = MyClass()
print(class3.counter)


print(class1.__dict__, class1.counter)
print(class2.__dict__, class2.counter)
print(class3.__dict__, class3.counter)