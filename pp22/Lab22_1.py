class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__salary = salary

    def get_salary(self):
        return round(self.__salary,1)

    def get_full_name(self):
        return '{} {}'.format(self.__first_name, self.__last_name)

    def get_age(self):
        return self.__age

    def raise_salary(self, increase = 10):
        self.__salary *= (1 + (increase / 100))


pracownik = Employee('Jan', 'Kowalski', 20, 4500)

print(pracownik.get_full_name(), "wiek:", pracownik.get_age(), "lat, pensja:", pracownik.get_salary())

#Pierwsza podwyżka - 15%

pracownik.raise_salary(15)

print(pracownik.get_full_name(), "wiek:", pracownik.get_age(), "lat, pensja:", pracownik.get_salary())


#Druga podwyżka - domyślne 10%

pracownik.raise_salary()

print(pracownik.get_full_name(), "wiek:", pracownik.get_age(), "lat, pensja:", pracownik.get_salary())









