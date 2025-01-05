# Napisz skrypt symulujący grę losową:
# użytkownik obstawia 6 liczb z 49,
# program losuje 6 liczb z 49,
# użytkownik dostaje informacje o ilości trafień

# Gra losowa
import random as rd

hits = 0
generated_numbers = []


print("Podaj 6 liczb całkowitych z zakresu od 1 do 49")

number_list = []

for i in range(6):
    print("Podaj", i + 1, "liczbę: ", end="")
    number = int(input())
    number_list.append(number)

number_list.sort()

print(number_list)


generated_numbers = rd.sample(range(1, 50), 6) #bez powtórzeń

generated_numbers.sort()

print(generated_numbers)






#Mechanizm sprawdzający

for number in number_list:
    if number in generated_numbers:
        hits += 1

print("Trafiono", hits, "razy." )










