from gc import get_stats


class Stack:      #Definiowanie klasy stosu

    def __init__(self):

        self.__stack_list = []

###################################################################################################

    def push(self, item):                       #Dodajemy metodę do umieszczania na stosie
        self.__stack_list.append(item)

    def pop(self):                              #Dodajemy metodę do sciągania ze stosu
        return self.__stack_list.pop()

    def get_stack_list(self):
        return self.__stack_list

    def print_stack(self):
        print(self.__stack_list)

####################################################################################################



Stack1 = Stack()
Stack2 = Stack()
Stack3 = Stack()


for i in range(1, 101):
    Stack1.push(i)

#print(Stack1.print_stack())

for i in range(len(Stack1.get_stack_list())):
    a = Stack1.pop()
    Stack2.push(a)

#print(Stack2.print_stack())


for i in range(len(Stack2.get_stack_list())):
    x = Stack2.pop()
    Stack3.push(x)

#print(Stack3.print_stack())


for i in range(len(Stack3.get_stack_list())):
    z = Stack3.pop()
    print(z, end = " ")



















