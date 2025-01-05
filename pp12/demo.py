#name = input("Jak masz na imie? ")
#print("Witaj {}!".format(name))


#Get and Show numbers"
#pobranie 3 liczb od iżutkowniak i wyświetlenie ich na ekranie

def get_number(number_no):
    print("Proszę, podaj {} liczbę: ".format(number_no))
    return int(input())

# a = get_number(1)
#
# b = get_number(2)
#
# c = get_number(3)

# print("Pobrano liczby:", a, b, c)


print("Pobrano liczby:", get_number(1), get_number(2), get_number(3))




