import random as rd

#maszyna losuje liczbe
number = rd.randint(1, 10)
msg = "Jak myślisz, jaka to liczba? Wpisz ją tutaj: "


if number % 2 == 0:
    parzystosc = "jest parzysta."
else:
    parzystosc = "nie jest parzysta."

#Gracz podaje pierwszą odpowiedź:

pierwsze = int(input("Wylosowano liczbę z zakresu od 1 do 10. Jak myślisz, jaka to liczba? Wpisz ją tutaj: "))

if number == pierwsze:
    print("Hurra, dobra odpowiedź!")
else:
    print("Niestety źle. Ta liczba ", parzystosc)
liczba = int(input(msg))


