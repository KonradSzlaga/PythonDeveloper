class Stack:      #Definiowanie klasy stosu

    def __init__(self):

        self.__stack_list = []

###################################################################################################

    def push(self, item):                       #Dodajemy metodę do umieszczania na stosie
        self.__stack_list.append(item)

    def pop(self):                              #Dodajemy metodę do sciągania ze stosu
        return self.__stack_list.pop()

    def empty(self):
        if len(self.__stack_list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.__stack_list)

    def top(self):
        try:
            return self.__stack_list[-1]
        except Exception as e:
            print(f"Top element annot be determined. Error: {e}")
####################################################################################################


stack1 = Stack()

print(stack1.empty())
print(stack1.size())
print(stack1.top())

for i in range(1, 101):
    stack1.push(i)

print(stack1.empty())
print(stack1.size())
print(stack1.top())