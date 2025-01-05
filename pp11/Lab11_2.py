# Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.



#1.Pobranie liczb od użytkownika
#2.Usuwanie duplikatów
#3.Sortowanie i wyświetlenie.
import random as rd


numbers = []

numbers_total = int(input("Ile liczb chcesz podać: "))

for i in range(numbers_total):
    number = int(input("Podaj " + str(i+1) + " element zbioru: " ))
    numbers.append(number)


numbers_distinct = []

for number in numbers:
    if number not in numbers_distinct:
        numbers_distinct.append(number)


numbers_distinct.sort(reverse=True)

print("Posortowany malejąco zbiór to:", numbers_distinct)
