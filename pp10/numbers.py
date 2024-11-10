#wylosuj 10 dowolnych liczb od 1 do 100 - umiesc je na liscie i wyswietl liste

import random as rd

numbers = []
counter = 0
while counter < 10:
    number = rd.randint(1, 100)
    numbers.append(number)
    counter += 1
print(numbers)

