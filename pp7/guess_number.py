import random

number = random.randint(1, 3)

#Użytkowinik podaje liczbe

guess = input("Zgadnij jaką liczbę mam na myśli (1, 2 lub 3): ")

if number == guess:
    print("Zgadłeś!!")
else:
    print("Niestety myślałem o liczbie", str(number), ".")