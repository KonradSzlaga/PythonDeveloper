#Wprowadzenie liczby:

liczba = int(input("Wprowadź liczbę do sprawdzenia: "))
wynik_pierwiastkowania = liczba ** (1/2)

if wynik_pierwiastkowania % 1 == 0:
 #   print("Pierwiastek kwadratowy wprowadzonej liczby jest liczbą całkowitą")
    str1 = "Tak"
    str2 = ""

else:
   # print("Pierwiastek kwadratowy wprowadzonej liczby nie jest liczbą całkowitą")

    str1 = "Nie"
    str2 = " nie"

print(str1 + ", pierwiastek kwadratowy w liczby " + str(liczba) + str2 + " jest liczbą całkowitą.")