#Ilosc punktow z kolokwium:

punkty = int(input("Podaj ilośc punktów procentowych studenta otrzymanych na kolokwium: "))

print("Student otrzymuje ocenę", end = " ")
if punkty >= 95:
    print("5,0")

elif punkty > 84:
    print("4,5")

elif punkty >= 70:
    print("4,0")

elif punkty > 60:
    print("3,5")

elif punkty > 50:
    print("3,0")

else:
    print("2,0")
