# def show_numbers(numbers):
#     print(numbers)
#
# show_numbers([1,2,3])
#
from pp11.Lab11_2 import numbers_total


##########################Zsumuj wszystkie elementy listy

# def sum_numbers(numbers_list):
#
#     sum = 0
#     for i in numbers_list:
#         sum += i
#     return sum
#
#
# c = sum_numbers([1,2,3,4,5,6,7,8,9])
#
# print(c)




####################### Losowanie dowolnej liczby z zakresu 1 do 99


# import random as rd
#
# def generate (number_numbers):
#     numbers = []
#
#     for i in range(number_numbers):
#         numbers.append(rd.randint(1,99))
#
#     return numbers
#
#
# print(generate(10))
# print(generate(5))



##############################Zmienna lokalna
def scope_test():
    x = 123
    return x

x = 100

print(x)
print(scope_test())






















