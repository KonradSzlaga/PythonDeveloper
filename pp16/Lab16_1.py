import platform as pl
import math
import random as rd


print("Twój procesor to:", pl.processor())
print()
print("Losuję 3 niepowtarzające się liczby z zakresu 1 - 10:", rd.sample(range(1,11), 3))
print()
print("Sinus 90 stopni to:", math.sin(math.pi / 2))