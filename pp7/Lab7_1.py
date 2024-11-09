#Wprowadzenie liczby:

liczba = int(input("Wprowadź liczbę do sprawdzenia: "))
wynik_pierwiastkowania = liczba ** (1/2)

if wynik_pierwiastkowania % 1 == 0:
    print("Pierwiastek kwadratowy wprowadzonej liczby jest liczbą całkowitą")
else:
    print("Pierwiastek kwadratowy wprowadzonej liczby nie jest liczbą całkowitą")

