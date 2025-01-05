#pobierz 3 liczby całkowite reprezentujace odcinku\
#Sprawdz czy da sie podstawic trójkąt

a = int(input("podaj pierwszy bok trójkąta: "))
b = int(input("podaj drugi bok trójkąta: "))
c = int(input("podaj trzeci bok trójkąta: "))

if a+b >= c and a+c >= b and b+c >= a:
    print("Z podanych długości odcinków można zbudować trójkąt")
else:
    print("Z podanych długości odcinków nie można zbudować trójkąta.")
