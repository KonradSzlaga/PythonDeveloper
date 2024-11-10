#okreslanie zakresu przez użytkownika

base = int(input("Podaj początek zakresu liczb: "))


roof = int(input("Podaj koniec zakresu liczb: "))

print("Liczby z podanego przez Ciebie zakresu podzielne przez 3, 5 lub 7 to:")

counter = 0

if base < roof:
    for i in range(base, roof + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            print(i)
            counter += 1
    if counter == 0:
        print("Niestety nie ma takich liczb")

elif base > roof:
    for i in range(roof, base + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            print(i)
            counter += 1
    if counter == 0:
        print("Niestety nie ma takich liczb")
else:
    print("Podane liczby są sobie równe - nie ma możliwości utworzyć zakresu")