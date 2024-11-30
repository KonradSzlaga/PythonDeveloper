import random as rd

#maszyna losuje liczbe
number = rd.randint(1, 10)


#Gracz podaje pierwszą odpowiedź:
pierwsze = int(input("Wylosowano liczbę z zakresu od 1 do 10. Jak myślisz, jaka to liczba? Wpisz ją tutaj: "))
msg = "Jak myślisz, jaka to liczba? Wpisz ją tutaj: "

#Sprawdzam czy liczba jest parzysta, w razie gdyby trzeba było przeprowadzić kolejną rundę zgadywania
if number % 2 == 0:
    parzystosc = "jest parzysta."
else:
    parzystosc = "nie jest parzysta."


#Sprawdzam czy jest większa od 5.
if number > 5:
    wieksze = "jest większa od 5."
else:
    wieksze = "jest mniejsza lub równa 5."


#Porównuję wprowadzoną liczbę                       - 1 próba
if number != pierwsze:
    print("Niestety źle. Ta liczba", parzystosc)

    liczba = int(input(msg))
    if number != liczba:
        print("Niestety źle. Ta liczba", wieksze)
        liczba = int(input(msg))

        if number != liczba:
            print("Niestety źle. Ta liczba to", number)

        else:
            print("Hurra, dobra odpowiedź!")
    else:
        print("Hurra, dobra odpowiedź!")

else:
    print("Hurra, dobra odpowiedź!")



