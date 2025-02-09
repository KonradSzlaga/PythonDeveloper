from Demo import MyClass

obj = MyClass()
#obj.__my_private_method()     # Nie działa więc sprawdzmy co jest w klasie
print(MyClass.__dict__)
obj._MyClass__my_private_method()