

# 2. Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
# na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum,
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez
# użytkownika,
# • wyświetli wylosowane serie liczb.


import random as rd


print('Podaj zakres liczb który zostanie wykorzystany w następnych krokach:')
min = int(input('Podaj wartość minimum: '))
max = int(input('Podaj wartość maximum: '))

numbers = rd.randint(min, max)
series = rd.randint(min, max)

print('Ilość serii liczb do wylosowania, to:', series)
print('Ilość liczb do wylosowania w każdej serii, to:', numbers)


numer_listy_do_utworzenia = 0


for x in range(series):
    liczby = []
    for i in range(numbers):
        liczby.append(rd.randint(min, max))

    print(x+1, 'uzupełniona seria to:', liczby)