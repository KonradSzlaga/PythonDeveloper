#Ilosc punkt ow z kolokwium:

punkty = int(input("Podaj ilośc punktów procentowych studenta otrzymanych na kolokwium: "))


if punkty >= 95:
    print("Student otrzymuje ocenę 5.0")

elif punkty > 84:
    print("Student otrzymuje ocenę 4,5")

elif punkty >= 70:
    print("Student otrzymuje ocenę 4.0")

elif punkty > 60:
    print("Student otrzymuje ocenę 3.5")

elif punkty > 50:
    print("Student otrzymuje ocenę 3.0")

else:
    print("Student otrzymuje ocenę 2.0")