#operacje bitowe:

# a = 5
# b = 3
#
# #Mnożenie (koniunkcja) bitowa:
# print(a, "&", b, "=", a & b)
#
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a & b))



#Alternatywa bitowa

# a = 5
# b = 3

# print(a, "|", b, "=", a | b)
#
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a | b))


# #XOR bitowy - alternatywa rozłączna
#
# a = 5
# b = 3
#
# print(a, "^", b, "=", a ^ b)
#
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a ^ b))


#Przesunięcie bitowe >> lub <<

# a = 5
# b = 3
#
# print(a, ">>", "=", a >> b)
#
# print("{:08b}".format(a))
# print("-" * 8)
# print("{:08b}".format(a >> b))
#
#
#
# a = 5
# b = 3
#
# print(a, "<<", "=", a << b)
#
# print("{:08b}".format(a))
# print("-" * 8)
# print("{:08b}".format(a << b))


#
# #Negacja bitowa
#
# a = 5
# b = 3
#
# print("~", a, "=", ~a)
#
# print("{:08b}".format(a))
# print("-" * 8)
# print("{:08b}".format(~a))


for i in range(5, -6, -1):
    print("{0:08b} => {1:d}".format(i, i))












