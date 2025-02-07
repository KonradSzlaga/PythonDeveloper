class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self) :
        if self.name[-1].lower() == 'a':
            print(f"Studentka ma na imię {self.name} i ma {self.age} lat. ")
        else:
            print(f"Student ma na imię {self.name} i ma {self.age} lat. ")





Ania = Student("Ania", 18)
Pawel = Student("Pawel", 19)
Ola = Student("Ola", 20)

Ania.student_info()
Pawel.student_info()
Ola.student_info()