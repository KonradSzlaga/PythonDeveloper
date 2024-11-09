# skrypt pobiera liczbe i sprawdza czy jest parzysta i podzielna przez 5 i 7

x = int(input("Podaj liczbę do sprawdzenia: "))


if x % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba nie jest parzysta.")

if x % 5 == 0:
    print("Liczba jest podzielna przez 5.")
else:
    print("Liczba nie jest podzielna przez 5.")

if x % 7 == 0:
    print("Liczba jest podzielna przez 7.")
else:
    print("Liczba nie jest podzielna przez 7.")