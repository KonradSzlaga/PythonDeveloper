class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_full_name(self):
        return '{} {}'.format(self.__first_name, self.__last_name)

    def get_age(self):
        return self.__age
