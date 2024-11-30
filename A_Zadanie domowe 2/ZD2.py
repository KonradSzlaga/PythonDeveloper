import random as rd
liczby = []

print('Podaj zakres liczb który zostanie wykorzystany w następnych krokach:')
min = int(input('Podaj wartość minimum: '))
max = int(input('Podaj wartość maximum: '))

numbers = rd.randint(min, max)

print('Ilość liczb do wylosowania, to:', numbers)

for i in range(numbers):
    liczby.append(rd.randint(min, max))

print('Wylosowane liczby to:', liczby)