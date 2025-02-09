class NewClass():
    counter = 0
    def __init__(self):
        print("Initializing the NewClass class.")
        NewClass.counter += 1
        print(f"Number of instances created: {NewClass.counter}")



class1 = NewClass()
class2 = NewClass()
class3 = NewClass()
class4 = NewClass()
class5 = NewClass()
class6 = NewClass()
class7 = NewClass()
class8 = NewClass()