#Użytkownik podaje symbol

symbol = input("Wprowadź symbol do utworzenia macierzy: ") + " "
rozmiar = int(input("Wprowadź rozmiar boku macierzy do jej utworzenia: "))


for i in range(1, rozmiar +1):
    print(symbol * rozmiar, "", end="\n")


# print(rozmiar)
# print(symbol)#
