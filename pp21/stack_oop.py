class Stack:      #Definiowanie klasy stosu

    def __init__(self):     #Metoda konstruktora
        #Ta metoda jest wykonywana zawsze przy tworzeniu obiektu
        #Przykłąd do poniższe 2 linie:
        #print('Cześć')
#stack_obj = Stack()

        self.__stack_list = []      # dunder ('__') hermetyzuje liste w tym przypadku
        # Nie można jej modyfikować z zewnątrz

#Aby dostęp do listy był możli]wy, trzeba to zrobić pośrednio - przez metodę / y

###################################################################################################

    def push(self, item):                       #Dodajemy metodę do umieszczania na stosie
        self.__stack_list.append(item)

    def pop(self):                              #Dodajemy metodę do sciągania ze stosu
        return self.__stack_list.pop()

####################################################################################################

stack_obj = Stack()

# stack_obj.push(5)
# stack_obj.push(3)
# stack_obj.push(2)
# stack_obj.push(88)
#
# print(stack_obj.pop())
# print(stack_obj.pop())
# print(stack_obj.pop())
# print(stack_obj.pop())


#Tworzymy nową klasę dziedziczącą po Stack

class StackSum(Stack):
    def getSum(self):
        #return sum(self.__stack_list) - to nie działa
        #Żeby dostać się do tej nazwy trzeba zastosować następujące podejście:
        return sum(self._Stack__stack_list)

stack = StackSum()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.getSum())
