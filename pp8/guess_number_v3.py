#gra toczy się dopuki nie zzostanie odgadnięta liczba - do poprawy


import random as rd
couner = 1
number = rd.randint(1,10)

guess = int(input("Pomyślałem jakąś liczbę z zakresu 1 - 10. Powiedz, jaka to liczba? Wpisz ją tutaj: "))


while guess != number:
    guess = nowa_liczba
    couner += 1
else:
    print("Dobrze!")