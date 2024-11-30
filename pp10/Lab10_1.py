# 1. Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.

tabela_imion = []

ilosc = int(input("Ile imion chcesz podać: "))



for i in range(ilosc):
    print("Podaj", i + 1, "imię. ", end = "")
    name = input("Imię to: ")
    tabela_imion.append(name)

print("Imiona jakie podano to:")

for i in range(len(tabela_imion)):
    print(tabela_imion[i])

