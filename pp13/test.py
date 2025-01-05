# ##############################Zmienna lokalna
# def scope_test():
#     x = 123
#     return x
#
# x = 100
#
# print(x)
# print(scope_test())


#################################### Zmiana wartości

# def change_values(n):
#     print('Przed zmianą:', n)
#     n += 1
#     print('Po zmianie:', n)
#     return n
#
# value = 7
#
# print(change_values(7))
# print(value)


# #################################### Zmiana wartości - LISTA
#
# # nie odnośimy się do listy tylko do referencji do listy
# # my_list_1 traktowana jest jako zmienna lokalna
#
# def change_values(my_list_1):
#
#     my_list_1 = [0,0]
#
# my_list_2 = [1, 2]
#
# change_values(my_list_2)
# print(my_list_2)



#################################### Zmiana wartości - LISTA

# nie odnośimy się do listy tylko do referencji do listy# Nie możemy modyfikować całej listy, ale jej poszczególne
# elementy już tak

# def change_values(my_list_1):
#
#     my_list_1[0] = 999
#
# my_list_2 = [1, 2]
#
# change_values(my_list_2)
# print(my_list_2)




################################## Fibonacci

# Ciąg Fibonacciego n- ciąg zaczynającuy się od dwóch jedynek


# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     # wartości do zwrotu dla n = 0 i mniejszego od 3 zopstały podane powyżej
#     # teraz określamy jak podań wartość liczny na n-tym miejscu ciągu fibonacciego
#
#     elem_1 = elem_2 = 1
#     sum = 0
#
#     for i in range(3, n + 1):
#         sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, sum
#         # elem_1 = elem_2
#         # elem_2 = sum
#
#     return sum
#
# for x in range(1, 100):
#     print(x, '-->', fib(x))



############## REKURENCJA



# Ciąg Fibonacciego n- ciąg zaczynającuy się od dwóch jedynek


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    # wartości do zwrotu dla n = 0 i mniejszego od 3 zopstały podane powyżej
    # teraz określamy jak podań wartość liczny na n-tym miejscu ciągu fibonacciego - rekurencyjnie

    return fib(n-1) + fib(n-2)

for x in range(1, 15):
    print(x, '-->', fib(x))












